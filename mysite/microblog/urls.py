from django.conf.urls import url , include

from . import views

from rest_framework import routers, serializers

from microblog.views import * #UserGetViewSet, UserInsertViewSet, PostGetViewSet
router = routers.DefaultRouter()
router.register(r'users/get',UserGetViewSet,'user') #of the form /users/get/?username=USERNAME
router.register(r'users/insert',UserInsertViewSet,'user')
router.register(r'posts/get',PostGetViewSet,'post')#of the form /posts/get/?username=USERNAME&number=NUMBER
router.register(r'home',HomepageViewSet,'post') #home page /home/?username=USERNAME&number=NUMBER
router.register(r'saved',GetSavedPostViewSet,'saves') #home page /saved/?username=USERNAME&number=NUMBER
router.register (r'follow',FollowsViewSet,'follows') #/follow/?follower=FOLLOWER&following=FOLLOWING
router.register(r'posts/save',PostSaveViewSet,'saves')# saves the post /posts/save/?username=USERNAME&postid=POSTID
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^',include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
