from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import *
from .models import User, Post, Follows
from rest_framework import viewsets

class UserGetViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = User.objects.all().order_by('-user_name')
        username = self.request.query_params.get('username', None)

        if username is not None:
            queryset = queryset.filter(user_name = username)


        return queryset


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
        queryset = Post.objects.all().order_by('-timestamp')
        if username is not None:
            queryset = queryset.filter(creator=username)
        if number is not None:
            queryset = queryset[:number]
        return queryset

class HomepageViewSet(viewsets.ModelViewSet):
    serializer_class  =PostSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        users_following = Follows.objects.values_list('following').filter(follower=username)
        queryset = Post.objects.all().order_by('-timestamp').filter(creator__in= set(users_following))
        return queryset

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
