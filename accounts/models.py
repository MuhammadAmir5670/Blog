import os

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


def user_profile_image(instance, filename):
    filename, ext = os.path.splitext(filename)
    filename = instance.user.username + "-profile" + ext
    return os.path.join("user", filename)

def user_banner_image(instance, filename):
    filename, ext = os.path.splitext(filename)
    filename = instance.user.username + "-banner" + ext
    return os.path.join("user", filename)


class Porfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_image, default='profile-pic-default.jpg')
    banner = models.ImageField(upload_to=user_banner_image, default='banner-pic-default.jpg')
    bio = models.CharField(max_length=100, help_text="Short Bio (eg. I love cats and games)")
    country = models.CharField(max_length=100, help_text="Enter Your Country")
    city = models.CharField(max_length=100, help_text="Enter Your City")

    twitter_url = models.URLField(max_length=250, default="#",
                                   blank=True, null=True,
                                   help_text="Enter # if you don't have an account")
    instagram_url = models.URLField(max_length=250, default="#",
                                     blank=True, null=True,
                                     help_text="Enter # if you don't have an account")
    facebook_url = models.URLField(max_length=250, default="#",
                                    blank=True, null=True,
                                    help_text="Enter # if you don't have an account")
    github_url = models.URLField(max_length=250, default="#",
                                  blank=True, null=True,
                                  help_text="Enter # if you don't have an account")

    email_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username + "'s profile"
