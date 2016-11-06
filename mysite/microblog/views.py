from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import *
from .models import User, Post, Follows, Saves
from rest_framework import viewsets
from .logic import *
from django.shortcuts import render

def index(request):
    post_set = Post.objects.all()
    context = {'post_set': post_set}
    return render(request, 'microblog/index.html', context)

def getPosts(request):
    username = request.GET.get('username',None)
    number =  request.GET.get('number')
    post_set= getPostDetails(username,number)
    context = {'post_set':post_set}
    return render(request, 'microblog/postlist.html', context)
def getProfile(request):
    username = request.GET.get('username',None)
    user_details = getUserDetails(username)
    post_set  =getPostDetails(username,None)
    context =   {
                'user_details':user_details,
                'post_set':post_set
                }
    return render(request, 'microblog/profile.html',context)
def getSavedPosts(request):
    username = request.GET.get('username',None)
    number =  request.GET.get('number')
    post_set = getSavedPostsByUser(username,number)
    context = {'post_set':post_set}
    return render(request, 'microblog/postlist.html', context)
