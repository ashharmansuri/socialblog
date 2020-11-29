from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver
from .models import Profile,Post

#signals for profile and cover
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile created')

post_save.connect(create_user_profile,sender=User)

def update_user_profile(sender, instance,created ,**kwargs):
    if created == False:
     instance.profile.save()
     print('updated created')

post_save.connect(update_user_profile,sender=User)   


## signals for slug field
def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return  create_slug(instance,new_slug=new_slug)
    return slug    
    
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver,sender=Post)    