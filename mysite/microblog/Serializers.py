from rest_framework import serializers
from models import User, Post
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name','password','profile_pic','bio')

class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_id','creator','timestamp','privacy','post_content')
