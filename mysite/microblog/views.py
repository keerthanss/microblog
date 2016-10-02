from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import UserSerializer
from .models import User
from rest_framework import viewsets

class UserGetViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        #username = self.kwargs['username']
        queryset = User.objects.all().order_by('-user_name')#.filter(user_name=username)
        username = self.request.query_params.get('username', None)

        if username is not None:
            queryset = queryset.filter(user_name = username)
        return queryset

        return queryset

    #queryset= User.objects.all().order_by('-user_name').filter(user_name='deepak')
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

def index(request):
    return HttpResponse("Hello, world. You're at the microblog index.")
# Create your views here.
