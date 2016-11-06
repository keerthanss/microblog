from django.shortcuts import render, redirect
from django.http import HttpResponse
from .Serializers import *
from rest_framework import viewsets
from .forms import *
from django.http import HttpResponseRedirect
from .signIn import authenticate, register
from .logic import *
from .models import Post

def isAuthenticated(request):
    if request.user:
        if request.user.is_authenticated:
            return True
    return False

def loginpage(request):
    #check if it is a POST request
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, auto_id=False)
        login_form = LogInForm(request.POST, auto_id=False)
        #check if either form has data
        if login_form.is_valid():
            data = login_form.cleaned_data
            print authenticate(request,data['username'], data['password'])
            print login_form.cleaned_data
            #TODO: change redirect url
            #return HttpResponseRedirect('profile')
            return redirect('profile')
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
    if not isAuthenticated(request):
        return redirect('index')

    #publish a post
    if request.method == "POST":
        post_form = PostForm(request.POST, auto_id=False)
        if post_form.is_valid():
            content = post_form.cleaned_data['post_content']
            isPublic = post_form.cleaned_data['public_privacy']
            if content.strip() != "":
                privacy = Post.PUBLIC if isPublic else Post.PRIVATE
                username = request.user.username
                publishPost(u_username=username, u_post_content=content, u_privacy= privacy)
                print "Post published!"
            else:
                print "Empty post cannot be published"
        else:
            print "invalid data"
    else:
        post_form = PostForm()

    username = request.GET.get('username',None)
    number =  request.GET.get('number')
    post_set= getPostDetails(username,number)
    context = {'title' : 'Home', 'post_set':post_set, 'post_form':post_form}
    return render(request, 'microblog/homepage.html', context)

def getProfile(request):
    if not isAuthenticated(request):
        return redirect('index')
    username = request.GET.get('username',None)
    user_details = getUserDetails(username)
    post_set  =getPostDetails(username,None)
    context =   {
                'title' : 'Profile',
                'user_details':user_details,
                'post_set':post_set
                }
    return render(request, 'microblog/profile.html',context)

def getSavedPosts(request):
    if not isAuthenticated(request):
        return redirect('index')
    username = request.GET.get('username',None)
    number =  request.GET.get('number')
    post_set = getSavedPostsByUser(username,number)
    context = {'post_set':post_set}
    return render(request, 'microblog/postlist.html', context)
