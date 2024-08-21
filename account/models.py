from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.dispatch import receiver
from django.db.models.signals import post_save
"""
class User(AbstractUser):
    
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
"""
class User(AbstractUser):
    # groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    # user_permissions = models.ManyToManyField(
    # Permission, related_name='custom_user_permissions'
    # )
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50,default="",blank=True)
    reset_password_expire = models.DateTimeField(null=True,blank=True)


@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):

    print('instance',instance)
    user = instance

    if created:
        profile = Profile(user=user)  
        profile.save()