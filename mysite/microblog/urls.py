from django.conf.urls import url , include

from . import views

from rest_framework import routers, serializers

from microblog.views import UserGetViewSet, UserInsertViewSet
router = routers.DefaultRouter()
router.register(r'user/get',UserGetViewSet,'user')
router.register(r'user/insert',UserInsertViewSet,'user')

urlpatterns = [
    url(r'^',include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^$', views.index, name='index'),
]
