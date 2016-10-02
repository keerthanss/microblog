from __future__ import unicode_literals
from datetime import datetime
from django.db import models
#admin user deepak, password testtesttest
# Create your models here.
class User(models.Model):
    profile_name =models.CharField(
        max_length = 30
    )
    user_name= models.CharField(
        max_length = 30,
        primary_key = True)
    password= models.CharField(
        max_length = 30)
    profile_pic= models.CharField(max_length = 50)
    bio= models.CharField(max_length = 300)


class Post(models.Model):
    post_id = models.AutoField(
        primary_key = True
    )
    creator = models.ForeignKey(User)
    timestamp = models.DateTimeField(
        default = datetime.now)
    privacy = models.CharField(
        max_length = 5
    )
    post_content = models.CharField(
        max_length = 256
    )
