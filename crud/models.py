from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from django.utils import timezone


# Create your models here.

class Profile(models.Model):

    EDUCATION_CHOICE =(
    ('M.C.A','M.C.A'),
    ('B.C.A','B.C.A'),
    ('B.A','B.A'),
    ('M.A','M.A'),
    ('P.G','P.G'),
    ('HIGH SCHOOL','HIGH SCOOL'),
    ('SECONDARY','SECONDARY'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pro_image = models.ImageField(default='default.png',upload_to='profileimage',blank=True)
    bio = models.CharField(max_length=250, blank=True)
    works = models.CharField(max_length=100,blank=True)
    cover = models.ImageField(default='default.png',upload_to='coverimage',blank=True)   
    birthday = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=50,choices= EDUCATION_CHOICE,blank=True)
    friends = models.ManyToManyField(User,blank=True,related_name='friends')
    
    def __str__(self):
        return f"{self.user.username}"


    def get_post_no(self):
        return self.posts.all().count()
  

    def get_likes_given_no(self):
        likes = self.like_set.all()       
        total_liked =0
        for item in likes:
            if item.value=='like':
              total_liked += 1
        return total_liked

      
    def get_likes_recieved_no(self):
        posts = self.posts.all()
        total_liked =0
        for item in posts:
            total_liked +=item.liked.all().count()
        return total_liked  





class Post(models.Model):
    title= models.CharField(max_length=100)
    content= RichTextField(blank=True,null=True)
    short_description = models.TextField(max_length=200,blank=True)
    post_image = models.ImageField(upload_to='postimages')
    liked = models.ManyToManyField(Profile,blank=True,related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    
    # class Meta:
    #     ordering =['-timestamp']   

    def num_likes(self):
        return self.liked.all().count()  
    
    def num_comments(self):
        return self.comment_set.all().count()
    
    def __str__(self):
        return self.title





    
class Photo(models.Model):
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)
    gallary = models.FileField(upload_to='gallaries',blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.uploaded_by.username




class Like(models.Model):
    LIKE_CHOICES =(
        ('Like','Like'),
        ('Unlike','Unlike'),
    )

    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,max_length=8)
    updated = models.DateTimeField(auto_now=True)     
    created = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"  



class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)













 
  
      