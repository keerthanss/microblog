from django.conf.urls import url , include

from . import views, apis
from .apis import *

from rest_framework import routers, serializers

from .views import * #UserGetViewSet, UserInsertViewSet, PostGetViewSet
apirouter = routers.DefaultRouter()
apirouter.register(r'api/users/get',apis.UserGetViewSet,'user') #of the form /users/get/?username=USERNAME
apirouter.register(r'api/users/insert',UserInsertViewSet,'user')
apirouter.register(r'api/posts/get',PostGetViewSet,'post')#of the form /posts/get/?username=USERNAME&number=NUMBER
apirouter.register(r'api/homepage',HomepageViewSet,'post') #home page /home/?username=USERNAME&number=NUMBER
apirouter.register(r'api/saved',GetSavedPostViewSet,'saves') #home page /saved/?username=USERNAME&number=NUMBER
apirouter.register (r'api/follow',FollowsViewSet,'follow-user') #/follow/?follower=FOLLOWER&following=FOLLOWING
apirouter.register(r'api/posts/save',PostSaveViewSet,'saves')# saves the post /posts/save/?username=USERNAME&postid=POSTID



urlpatterns = [
    #url(r'index', views.index, name='index'),
    url(r'^$', views.loginpage, name='index'),
    #url(r'^',include(router.urls)),
    url(r'editprofile/', views.editProfile,name='editProfile'),
    url(r'posts/get', views.homepage,name='postlist'),
    url(r'profile/', views.getProfile,name='profile'),
    url(r'saved/', views.getSavedPosts,name='postlist'),
    url(r'home/', views.homepage, name='homepage'),
    #url(r'^',include(viewrouter.urls)),
    url(r'unfollow/', views.unfollow,name='unfollow'),
    url(r'follow/', views.follow,name='follow'),
    url(r'unsave/', views.unsave,name='unsave'),
    url(r'save/', views.save,name='save'),
    url(r'share/', views.share, name='share'),
    url(r'logout/', views.logoutview, name='logout'),
    url(r'^',include(apirouter.urls)),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
