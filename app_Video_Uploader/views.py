from django.shortcuts import render
from rest_framework import viewsets
from app_Video_Uploader.serializers import VideoSerializer
from .models import Video

# Create your views here.


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

