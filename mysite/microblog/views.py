from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import UserSerializer ,PostSerializer
from .models import User, Post
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
