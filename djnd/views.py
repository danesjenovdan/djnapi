from django.shortcuts import render

from rest_framework import viewsets

from .models import Video, Project, Clip, InfoPush
from .serializers import VideoSerializer, ProjectSerializer, ClipSerializer, InfoPushSerializer

# Create your views here.
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ClipViewSet(viewsets.ModelViewSet):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer

class InfoPushViewSet(viewsets.ModelViewSet):
    queryset = InfoPush.objects.all()
    serializer_class = InfoPushSerializer
