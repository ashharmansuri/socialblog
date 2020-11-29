from django.shortcuts import render,redirect
from urllib.parse import quote 
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Post,Profile,Photo,Like
from django.contrib.auth.models import User
from .forms import PostCreateForm,UserUpdateForm,ProfileForm,UserPasswordForm,GallaryForm,CommentForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from validate_email import validate_email
from .decorators import unauthenticated_user
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



# Create your views here.
@login_required(login_url='login')
def  home(request):
    qs_list = Post.objects.filter(draft=False)

    paginator= Paginator(qs_list,6)
    page = request.GET.get('page')
    try:
        qs =paginator.page(page)
    except PageNotAnInteger:
        qs =paginator.page(1)
    except EmptyPage:
        qs =paginator.page(paginator.num_pages)     
   
    context={
        'qs':qs
    }  
    return render(request,'crud/home.html',context)

# @login_required(login_url='login')
# def like_unlike_post(request):
#     user = request.user
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         post_obj = Post.objects.get(id=post_id)
#         profile = Profile.objects.get(user=user)

#         if profile in post_obj.liked.all():
#             post_obj.liked.remove(profile)
#         else:
#             post_obj.liked.add(profile)
#         like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

#         if not created:
#             if like.value=='Like':
#                 like.value='Unlike'
#             else:
#                 like.value='Like'
#         else:
#             like.value='Like'
#             post_obj.save()
#             like.save()

   


@login_required(login_url='login')
def like_unlike_post(request):
    user=request.user
    if request.method=="POST":
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like,created = Like.objects.get_or_create(user=profile,post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value ='Unlike'
            else: 
                like.value = 'Like'   
        else:
            like.value='Like'    

            post_obj.save()
            like.save()    
    return redirect('post-detail',pk=post_id)


@login_required(login_url='login')
def PostDetailView(request,pk):
    form = CommentForm()
    post = Post.objects.get(id=pk)
    print('mypost:',post)
    latest_post = Post.objects.all().order_by('-timestamp')[0:5]
    share_string = quote(post.content)

    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
        form = CommentForm()
        return redirect('post-detail',pk=pk)

    context ={'obj':post,'latest_post':latest_post,'form':form,'profile':profile,'share_str':share_string}
    return render(request,'crud/post_detail.html',context)



@login_required(login_url='login')
def PostCreateView(request):
    fm = PostCreateForm()
    if request.method=="POST":
        fm = PostCreateForm(request.POST,request.FILES)
        if fm.is_valid():
            user_post =fm.save(commit=False)
            user_post.author = request.user
            user_post.save()
            messages.success(request,'you have made post succesfully')
            return redirect('home')
    context ={'form':fm}
    return render(request,'crud/post_create.html',context)
    

@login_required(login_url='login')
def PostUpdateView(request,slug=None):
    post = Post.objects.get(slug=slug)
    fm = PostCreateForm(instance=post)
    if request.method=="POST":
        fm = PostCreateForm(request.POST,request.FILES,instance=post)
        if fm.is_valid():
            user_post=fm.save(commit=False)
            user_post.author = request.user
            user_post.save()
            messages.success(request,'You have Updated post succesfully')
            return redirect('home')

    context ={'form':fm}
    return render(request,'crud/post_create.html',context)

@login_required(login_url='login')
def PostDeleteView(request,slug=None):
    post = Post.objects.get(slug=slug)
    post.delete()
    messages.error(request ,'You have deleted Your Post')
    return redirect('dashboard')


@login_required(login_url='login')
def PostSearchView(request):
    search_query = request.GET.get('search-query')
    print(search_query)
    allpoststitle = Post.objects.filter(title__icontains=search_query)
    allpostsdesc = Post.objects.filter(short_description__icontains=search_query)
    allposts = allpoststitle.union(allpostsdesc)

    context = {'posts':allposts,'search_query':search_query}
    return render(request, 'crud/post_search.html',context)



def ContactView(request):
    if request.method=='POST':
        sendername = request.POST.get('sender_name')
        print(sendername)
    return render(request,'crud/contactus.html')


# def Account_Settings(request):
#     user_form = UserUpdateForm(instance=request.user)
#     profile_form = ProfileForm(instance= request.user.profile)
#     pass_form = UserPasswordForm(request.user)

#     if request.method=='POST':
        
#         user_form = UserUpdateForm(request.POST,instance=request.user)
#         profile_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
            
#             messages.success(request,'Your Profile has been Updated')
#             # return HttpResponseRedirect(reverse('user-profile',args=[int(request.user.id)]))
#             return redirect('account-settings')
    
#     if request.method=="POST":
        
#             form = UserPasswordForm(request.user,request.POST)
#             if form.is_valid():
#                 pc= form.save()
                
#                 update_session_auth_hash(request,pc)
#                 messages.info(request,'Password Changed successfully')
#                 return redirect('password-change')   

#     context ={'user_form':user_form,'profile_form':profile_form,'pass_form':form}
#     return render(request,'crud/account_settings.html',context)



@login_required(login_url='login')
def Account_Settings(request):
    
    # initials
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileForm(instance= request.user.profile)
    pass_form = UserPasswordForm(request.user)
    
    if "submit_pro_form" in request.POST:
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
    
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            user_form = UserUpdateForm(instance=request.user)
            profile_form.save()
            profile_form = ProfileForm(instance= request.user.profile)
                
            messages.success(request,'Your Profile has been Updated')
            # return HttpResponseRedirect(reverse('user-profile',args=[int(request.user.id)]))
            return redirect('account-settings')
    
   
    if "submit_pass_form" in request.POST:  
        pass_form = UserPasswordForm(request.user,request.POST)

        if pass_form.is_valid():
            pc= pass_form.save()
            form = UserPasswordForm(request.user)
                    
            update_session_auth_hash(request,pc)
            messages.info(request,'Password Changed successfully')
            return redirect('account-settings')   

    context ={
        'user_form':user_form,
        'profile_form':profile_form,
        'pass_form':pass_form
        }

    return render(request,'crud/account_settings.html',context)


@login_required(login_url='login')
def photos_gallary(request):
    user_images = Photo.objects.filter(uploaded_by = request.user)
    gallary_form = GallaryForm()
    if request.method=="POST":
        gallary_form = GallaryForm(request.POST,request.FILES)
        files = request.FILES.getlist('gallary')
        gallary_form.save(commit=False)
        
        if gallary_form.is_valid():
            for f  in files:
                current_user = request.user
                images = Photo(uploaded_by=current_user,gallary=f)
                user_photo=images.save()
    context ={'g_form':gallary_form,'user_photos':user_images}
    # print(user_images)
    return render(request,'crud/upload_photos.html',context)

@login_required(login_url='login')
def user_photos_gallary(request,pk):
  images = Photo.objects.filter(uploaded_by = pk)
  context ={'user_photos':images}
  print('images:',images)
  return render(request,'crud/user-upload-photos.html',context)



@login_required(login_url='login')
def Dashboard(request):
    current_user = request.user
    count = Post.objects.filter(author=current_user).count()
    user_post = Post.objects.filter(author=current_user).order_by('-timestamp')
    context = {'posts':user_post,'counts':count}
    return render(request,'crud/dashboard.html',context)

@login_required(login_url='login')
def User_Profile(request,pk):
    user = User.objects.get(id=pk)
    context ={'user_info':user}
    return render(request,'crud/user_profile.html',context)



# def UserPasswordChange(request):
#     form = UserPasswordForm(request.user)
#     if request.method=="POST":
#         pass_form = UserPasswordForm(request.user,request.POST)
#         if pass_form.is_valid():
#             pc= pass_form.save()
            
#             update_session_auth_hash(request,pc)
#             messages.info(request,'Password Changed successfully')
#             return redirect('password-change')

#     context ={'pass_form':pass_form}
#     return render(request,'crud/password_change.html',context)



@csrf_exempt
def emailValidationView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'email is invalid'},status=400)
        if User.objects.filter(email=email).exists():   
             return JsonResponse({'email_error':'email is taken already'},status=409)
        return JsonResponse({'email_valid':True},status=400)


@csrf_exempt
def usernameValidationView(request):
    if request.method=="POST":
        data = json.loads(request.body)
        print(data)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should contain alphanumeric only'},status=400)
        if User.objects.filter(username=username).exists():   
             return JsonResponse({'username_error':'username is taken already'},status=409)
        return JsonResponse({'username_valid':True},status=400)    


@unauthenticated_user
def User_Login_Register(request):
    #initials
    

    if "submit_login_form" in request.POST:
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You are logged in succesfully')
            return redirect('home')
    
    if "submit_register_form" in request.POST:

        username = request.POST.get('username')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        context = {
            'fieldValue':request.POST
            }
        if password1 != password2:
            messages.error(request,'password does not match')
            return redirect('login')    
        if len(username)<4:
            messages.error(request,'username must contain more than 4 character')
            return redirect('login')  
        elif  not str(username).isalnum():
            messages.error(request,'username can contain only Alphanumerical')
            return redirect('login')       
        elif User.objects.filter(username=username).exists():
            messages.error(request,'username is taken already')
            return redirect('login') 
        elif User.objects.filter(email=email).exists():
            messages.error(request,'email is taken already')
            return redirect('login')     
        else:
            print(username,fname,lname,email,password1)   
            user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password1)
            user.save()
            messages.success(request,'Your Account Has Been Create Succesfully')
            return redirect('login')
        

    return render(request,'accounts/login_register.html')    


def User_Logout(request):
    logout(request)
    messages.info(request, 'You are logged out succesfully')
    return redirect('login')

