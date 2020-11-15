from django.contrib import admin
from .models import Post,Profile,Photo,Like,Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display=['id','title','content','author','short_description','post_image','timestamp']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display=['id','user','pro_image','bio','birthday','works','education','cover']    


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=['uploaded_by','gallary','upload_time']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['user','post','value','updated','created']    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['user','post','body','updated','created']      