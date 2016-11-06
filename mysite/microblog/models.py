from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User as auth_user

#admin user deepak, password testtesttest
# Create your models here.
class User(models.Model):
    profile_name =models.CharField(
        max_length = 30
    )
    user_name= models.CharField(
        max_length = 30,
        primary_key = True)
    userid = models.OneToOneField(auth_user, default=-1)
    profile_pic = models.CharField(max_length = 50)
    bio = models.CharField(max_length = 300)


class Post(models.Model):
    post_id = models.AutoField(
        primary_key = True
    )
    creator = models.ForeignKey(User)
    timestamp = models.DateTimeField(
        default = datetime.now)
    privacy = models.CharField(
        max_length = 10,
        default="pub"
    )
    post_content = models.CharField(
        max_length = 256
    )

class Follows(models.Model):
    follower = models.ForeignKey(User,related_name='post_follower')
    following = models.ForeignKey(User,related_name='post_creator')

class Saves(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    timestamp = models.DateTimeField(
        default = datetime.now)
