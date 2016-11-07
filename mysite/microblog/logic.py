from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import *
from .models import User, Post, Follows, Saves, Shares
from rest_framework import viewsets
def getPostDetails(username,number):
    queryset = Post.objects.all().order_by('-timestamp')
    if username is not None:
        queryset = queryset.filter(creator=username)
    if number is not None:
        queryset = queryset[:number]
    return queryset
def addSavedFieldToPostList(post_set, username):
    saved_post_set = getSavedPostsByUser(username,None)
    for post in post_set:
        saved = False
        for saved_post in saved_post_set:
            if saved_post.post_id == post.post_id:
                saved = True
        post.saved=saved
    return post_set
def getUserDetails(username):
    queryset = User.objects.all().order_by('-user_name')
    if username is not None:
        queryset = queryset.filter(user_name = username)
    #else:
    #    queryset = queryset [:0]
    return queryset
def savePost(user,post):
    user = User.objects.get(user_name = user)
    post = Post.objects.get(post_id = post)
    if user is not None and post is not None:
        postsSaved= Saves.objects.all().filter(user=user)
        postsSaved= postsSaved.filter(post=post)
        if len(postsSaved)>0:
            return True
        savePost=Saves(user=user,post=post)
        savePost.save()
        return True

def unsavePost(user,post):
        user = User.objects.get(user_name = user)
        post = Post.objects.get(post_id = post)

        postsSaved= Saves.objects.all().filter(user=user)
        postsSaved= postsSaved.filter(post=post)

        if postsSaved:
            postsSaved.delete()
        return True


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

def sharePost(user, post):
    print "user " + str(user) + " wants to share post " + str(post)
    _user = User.objects.get(user_name=user)
    _post = Post.objects.get(post_id=post)
    if _user is not None and _post is not None:
        share = Shares(user=_user, post=_post)
        share.save()
