from django.contrib.auth.models import User as auth_user
from django.contrib.auth import authenticate as authenticateUser
from django.contrib.auth import login as logInUser
from django.contrib.auth import logout
from .models import User

def authenticate(request, u_username, u_password):
    user = authenticateUser(username=u_username, password=u_password)
    if user is not None:
        logInUser(request, user)
        print "Logged in!"
        return True
    else:
        return False

def register(u_email, u_username, u_password):
    newuser = auth_user.objects.create_user(email=u_email, username=u_username, password=u_password)
    newuser_infoentry = User(user_name = newuser.username, userid_id = newuser.id)
    newuser.save()
    newuser_infoentry.save()
    print "New user created!"

def logoutuser(request):
    print "Logging out " + str(request.user.username)
    logout(request)
    print "Logged out"
