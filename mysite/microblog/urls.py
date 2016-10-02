from django.conf.urls import url , include

from . import views

from rest_framework import routers, serializers

from microblog.views import * #UserGetViewSet, UserInsertViewSet, PostGetViewSet
router = routers.DefaultRouter()
router.register(r'users/get',UserGetViewSet,'user')
router.register(r'users/insert',UserInsertViewSet,'user')
router.register(r'posts/get',PostGetViewSet,'post')
router.register(r'home',HomepageViewSet,'post') #home page
router.register (r'follow',FollowsViewSet,'follows')

urlpatterns = [
    url(r'^',include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
