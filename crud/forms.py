from django import forms
from .models import Post,Profile,Photo,Comment
# from tinymce.widgets import TinyMCE
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
import datetime

class UserRegisterationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-Enter Password'}))
    joined_date = datetime.datetime.now()
    class Meta:
        model=User
        fields =['username','email','first_name','last_name']
        widgets ={
             'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
             'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name'}),
             'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),
             'email':forms.TextInput(attrs={'placeholder':'Enter Email'}),
             }

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','post_image','short_description']         
        widgets ={
             'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Post Title'}),
             'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Write Post Content....'}),
             'post_image':forms.FileInput(attrs={'class':'form-control-file'}),
             'short_description':forms.Textarea(attrs={'class':'form-control','rows':3,'cols':3,'placeholder':'Short description....'}),
            #  'draft':forms.CheckboxInput(attrs={'class':'form-control-input'}),
            #  'publish':forms.TextInput(attrs={'class':'form-control','type':'date'}),
             }    


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields =['username','email','first_name','last_name']
        widgets ={
             'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
             'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
             'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
             'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
             }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['pro_image','bio','birthday','education','works','cover']
        widgets ={
                'pro_image':forms.FileInput(attrs={'class':'form-control-file'}),
                'bio':forms.TextInput(attrs={'class':'form-control'}),
                'birthday':forms.TextInput(attrs={'class':'form-control','type':'date'}),
                'works':forms.TextInput(attrs={'class':'form-control'}),
                'education':forms.Select(attrs={'class':'form-control'}),
                'cover':forms.FileInput(attrs={'class':'form-control-file'}),
                'birthday':forms.TextInput(attrs={'class':'form-control','type':'date'}),
        }

class UserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))            



class GallaryForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=['gallary']
        widgets ={
            'gallary':forms.FileInput(attrs={'class':'form-control-file','multiple':True})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body',]
        labels ={'body':''}
        widgets ={
            'body':forms.TextInput(attrs={'class':'form-control','id':'comment_input','placeholder':'Add Comment...'})
        }

