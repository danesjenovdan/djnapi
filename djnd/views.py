from django.shortcuts import render

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, Filter, FilterSet
from taggit.forms import TagField

from .models import Video, Project, Clip, InfoPush
from .serializers import VideoSerializer, ProjectSerializer, ClipSerializer, InfoPushSerializer


# FILTERS

class TagsFilter(Filter):
    field_class = TagField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)


class ClipFilterSet(FilterSet):
    tags = TagsFilter(field_name='tags__name')
    languages = TagsFilter(field_name='languages__name')
    formats = TagsFilter(field_name='formats__name')
    types = TagsFilter(field_name='types__name')

    class Meta:
        model = Clip
        fields = ()  # add model fields here


# VIEWS

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
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = ClipFilterSet
    ordering_fields = ('order', 'date',)
    ordering = ('order',)

class InfoPushViewSet(viewsets.ModelViewSet):
    queryset = InfoPush.objects.all()
    serializer_class = InfoPushSerializer
