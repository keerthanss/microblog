from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import *
from .models import User, Post, Follows, Saves
from rest_framework import viewsets
def getPostDetails(username,number):
    queryset = Post.objects.all().order_by('-timestamp')
    if username is not None:
        queryset = queryset.filter(creator=username)
    if number is not None:
        queryset = queryset[:number]
    return queryset

def getUserDetails(username):
    queryset = User.objects.all().order_by('-user_name')
    if username is not None:
        queryset = queryset.filter(user_name = username)
    #else:
    #    queryset = queryset [:0]
    return queryset

def getSavedPostsByUser(username,number):
    if username is None:
        return None
    postsSaved= Saves.objects.all().filter(user=username)
    l =[]
    for p in postsSaved:
        l.insert(0,p.post_id)

    queryset = Post.objects.all().order_by('-timestamp').filter(post_id__in= set(l))

    if number is not None:
        queryset = queryset[:number]
    return queryset

def publishPost(u_username, u_post_content, u_privacy=Post.PUBLIC):
    author = getUserDetails(u_username).first()
    new_post = Post(creator=author, privacy=u_privacy, post_content=u_post_content)
    new_post.save()
