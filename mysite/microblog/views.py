from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .Serializers import *
from rest_framework import viewsets
from .forms import *
from django.http import HttpResponseRedirect
from .signIn import authenticate, register
from .logic import *
from .models import Post
from django.http import HttpResponseRedirect
from .signIn import authenticate, register, logoutuser
from .logic import *
from .forms import *
from django.contrib import messages



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
            return redirect('homepage')
        elif register_form.is_valid():
            data = register_form.cleaned_data
            register(data['r_email'], data['r_username'], data['r_password'])
            print register_form.cleaned_data
            #TODO: change redirect url
            return redirect('index')
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
def editProfile(request):
    username = request.user.username

    user_details = getUserDetails(username).first()
    #return render (request, 'microblog/editprofile.html',context)

    if request.method == 'POST':
        print "Received post method"
        form=EditProfileForm(request.POST, request.FILES)
        print form
        if form.is_valid():
            print "Form is valid"
            if request.FILES['profile_pic']:
                user_details.profile_pic=request.FILES['profile_pic']
            #saveProfilePic(request.user.username, request.FILES['profile_pic'])
            form=form.cleaned_data
            user_details.profile_name=form['profile_name']
            user_details.bio=form['bio']
            user_details.save()
            return HttpResponseRedirect('/microblog/profile')

    else:
        form = EditProfileForm(initial={'profile_name': user_details.profile_name ,'bio':user_details.bio})

    return render(request, 'microblog/editprofile.html', {'form': form, 'searchForm':SearchForm()})

def searchUser(request):
    if request.method == 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            form=form.cleaned_data
            user_name=form['searchField']
            if userNameIsValid(user_name):
                return HttpResponseRedirect('/microblog/profile/?username='+user_name)
            messages.add_message(request, messages.INFO, 'User not found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def homepage(request):
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

    username = request.user.username
    number =  request.GET.get('number')
    post_set= getHomePagePosts(username,number)

    post_set = addSavedFieldToPostList(post_set,request.user.username)
    context = {'title' : 'Home', 'post_set':post_set, 'post_form':post_form,'searchForm':SearchForm(),}
    return render(request, 'microblog/homepage.html', context)

def logoutview(request):
    logoutuser(request)
    return redirect('index')

def unfollow(request):
    follower=request.user.username
    following= request.GET.get('following', None)
    unfollowUser(follower,following)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def deletePost(request):
    username = request.user.username
    postid= request.GET.get('post',None)
    deletePostLogic(postid,username)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def follow(request):
    follower=request.user.username
    following= request.GET.get('following', None)
    followUser(follower,following)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def save(request):

    user = request.user.username
    post = request.GET.get('post',None)
    savePost(user,post)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unsave(request):
    user = request.user.username
    post = request.GET.get('post',None)

    unsavePost(user,post)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def share(request):
    user = request.user.username
    post = request.GET.get('post', None)
    sharePost(user, post)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def getProfile(request):
    if not isAuthenticated(request):
        return redirect('index')
    username = request.GET.get('username',None)
    isUsersProfile=False
    if username == request.user.username:
        isUsersProfile=True
    if username ==None:
        username = request.user.username
        isUsersProfile=True
    isFollowing = checkFollowing(request.user.username,username)
    user_details = getUserDetails(username)
    #post_set  =getPostDetails(username,None)
    #post_set = addSavedFieldToPostList(post_set,request.user.username)
    post_set = getPostsForProfilePage(username,None, isUsersProfile)

    context =   {
                'isfollowing':isFollowing,
                'myprofile': isUsersProfile,
                'title' : 'Profile',
                'profiletab':'all',
                'user_details':user_details,
                'searchForm':SearchForm(),
                'post_set':post_set
                }
    return render(request, 'microblog/profile.html',context)

def profilePageSavedPosts(request):
    if not isAuthenticated(request):
        return redirect('index')
    username = request.user.username
    user_details = getUserDetails(username)
    number =  request.GET.get('number')
    post_set = getSavedPostsByUser(username,number)
    for post in post_set:
        post.saved=True
    context = {
                'myprofile':True,
                'title':'Profile',
                'user_details':user_details,
                'profiletab':'saved',
                'post_set':post_set,
                'searchForm' : SearchForm()
                }
    return render(request, 'microblog/profile.html', context)

def profilePageSharedPosts(request):
    if not isAuthenticated(request):
        return redirect('index')
    username = request.user.username
    user_details = getUserDetails(username)
    number =  request.GET.get('number')
    post_set = getSharedPostsByUser(username,number)
    context = {
                'myprofile':True,
                'title':'Profile',
                'user_details':user_details,
                'profiletab':'shared',
                'post_set':post_set
                }
    return render(request, 'microblog/profile.html', context)
