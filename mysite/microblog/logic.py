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
def followUser(follower,following):
    isFollowing=checkFollowing(follower,following)
    if isFollowing:
        return True
    followerObject = User.objects.get(user_name = follower)
    followingObject = User.objects.get(user_name = following)
    if followerObject is not None and followingObject is not None:
            follow = Follows(follower=followerObject,following=followingObject)
            follow.save()
    return True
def unfollowUser(follower,following):
    followerObject = User.objects.get(user_name = follower)
    followingObject = User.objects.get(user_name = following)
    allFollowing = Follows.objects.all().filter(follower=followerObject)
    allFollowing = allFollowing.filter(following = followingObject)
    if allFollowing:
        allFollowing.delete()
    return True

def checkFollowing(follower, following):
    followerObject = User.objects.get(user_name = follower)
    followingObject = User.objects.get(user_name = following)
    allFollowing = Follows.objects.all().filter(follower=followerObject)
    allFollowing = allFollowing.filter(following = followingObject)
    if len(allFollowing) >0:
        return True
    return False
