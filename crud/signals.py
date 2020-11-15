from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#signals
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