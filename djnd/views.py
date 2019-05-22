from django.shortcuts import render

from rest_framework import viewsets, filters

from .models import Video, Project, Clip, InfoPush
from .serializers import VideoSerializer, ProjectSerializer, ClipSerializer, InfoPushSerializer

# Create your views here.
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('order', 'date',)
    ordering = ('order',)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('order', 'date',)
    ordering = ('order',)

class ClipViewSet(viewsets.ModelViewSet):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('order', 'date',)
    ordering = ('order',)

class InfoPushViewSet(viewsets.ModelViewSet):
    queryset = InfoPush.objects.all()
    serializer_class = InfoPushSerializer
