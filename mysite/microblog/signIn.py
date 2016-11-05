from django.contrib.auth.models import User
from django.contrib.auth import authenticate as authenticateUser
from django.contrib.auth import login as logInUser

def authenticate(request, u_username, u_password):
    user = authenticateUser(username=u_username, password=u_password)
    if user is not None:
        logInUser(request, user)
        print "Logged in!"
        return True
    else:
        return False

def register(u_email, u_username, u_password):
    newuser = User.objects.create_user(u_email, u_username, u_password)
    newuser.save()
    print "New user created!"
