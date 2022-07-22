from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('video', views.VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]