from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import *
from .models import User, Post, Follows, Saves
from rest_framework import viewsets
from logic import *



class UserGetViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):


        username = self.request.query_params.get('username', None)

        return getUserDetails(username)


class UserInsertViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        password = self.request.query_params.get('password', None)
        pic = self.request.query_params.get('pic', None)
        bio =self.request.query_params.get('bio', None)
        user = User(username,password,pic,bio)
        user.save()
        queryset = User.objects.all()
        return queryset

class PostGetViewSet (viewsets.ModelViewSet):
    serializer_class = PostSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        number = self.request.query_params.get('number', None)
        return getPostDetails(username,number)



class FollowsViewSet(viewsets.ModelViewSet):
    serializer_class=FollowsSerializer
    def get_queryset(self):
        followerUsername=self.request.query_params.get('follower', None)
        followerObject = User.objects.get(user_name = followerUsername)
        followingUsername = self.request.query_params.get('following', None)
        followingObject = User.objects.get(user_name = followingUsername)

        #avoid duplicates
        allFollowing = Follows.objects.all().filter(follower=followerObject)
        allFollowing = allFollowing.filter(following = followingObject)
        if len(allFollowing) >0:
            return allFollowing

        #avoid a person following themselves
        if followerObject ==followingObject:
            return allFollowing
        if followerObject is not None and followingObject is not None:
            follow = Follows(follower=followerObject,following=followingObject)
            follow.save()
        queryset = Follows.objects.all().order_by('-id')[:1]
        return queryset

class PostSaveViewSet(viewsets.ModelViewSet):
    #user specified by username saveas the post specified by postid
    serializer_class = SavesSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username',None)
        postid = self.request.query_params.get('postid',None)
        user = User.objects.get(user_name = username)
        post = Post.objects.get(post_id = postid)

        if user is not None and post is not None:
            postsSaved= Saves.objects.all().filter(user=user)
            postsSaved= postsSaved.filter(post=post)
            if len(postsSaved)>0:
                return postsSaved
            savePost=Saves(user=user,post=post)
            savePost.save()

        queryset = Saves.objects.all().order_by('-timestamp')[:1]
        return queryset

class HomepageViewSet(viewsets.ModelViewSet):
    serializer_class  =PostSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        number = self.request.query_params.get('number', None)
        users_following = Follows.objects.values_list('following').filter(follower=username)
        queryset = Post.objects.all().order_by('-timestamp').filter(creator__in= set(users_following))
        if number is not None:
            queryset = queryset[:number]

        return queryset

class GetSavedPostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username',None)
        number = self.request.query_params.get('number', None)
        return getSavedPostsByUser(username,number)
