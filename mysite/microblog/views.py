from django.shortcuts import render
from django.http import HttpResponse
from .Serializers import *
from rest_framework import viewsets
from .forms import LogInForm, RegisterForm
from django.http import HttpResponseRedirect
from .signIn import authenticate, register
from .logic import *

def loginpage(request):
    #check if it is a POST request
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, auto_id=False)
        login_form = LogInForm(request.POST, auto_id=False)
        #check if either form has data
        if login_form.is_valid():
            data = login_form.cleaned_data
            authenticate(request,data['username'], data['password'])
            print login_form.cleaned_data
            #TODO: change redirect url
            return HttpResponseRedirect('/success')
        elif register_form.is_valid():
            data = register_form.cleaned_data
            register(data['r_email'], data['r_username'], data['r_password'])
            print register_form.cleaned_data
            #TODO: change redirect url
            return HttpResponseRedirect('/registered')
        else: #none of the forms have valid data
            print "invalid form"
    #work with the GET request
    else:
        register_form = RegisterForm()
        login_form = LogInForm()
        context = {'login_form' : login_form, 'register_form' : register_form}
    return render(request, 'microblog/login.html', context);

'''
def index(request):
    post_set = Post.objects.all()
    context = {'post_set': post_set}
    return render(request, 'microblog/index.html', context)
'''

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
