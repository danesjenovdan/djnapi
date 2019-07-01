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

class VideoFilterSet(FilterSet):
    tags = TagsFilter(field_name='tags__name')

    class Meta:
        model = Video
        fields = ()  # add model fields here

class ProjectFilterSet(FilterSet):
    tags = TagsFilter(field_name='tags__name')

    class Meta:
        model = Project
        fields = ()  # add model fields here

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
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = VideoFilterSet
    ordering_fields = ('order', 'date',)
    ordering = ('order',)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data.update({
            'filters': {
                'tags': list(Video.tags.most_common().values_list('name', flat=True).order_by('id')),
            }
        })
        return response

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = ProjectFilterSet
    ordering_fields = ('order', 'date',)
    ordering = ('order',)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data.update({
            'filters': {
                'tags': list(Project.tags.most_common().values_list('name', flat=True).order_by('id')),
            }
        })
        return response

class ClipViewSet(viewsets.ModelViewSet):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = ClipFilterSet
    ordering_fields = ('order', 'date',)
    ordering = ('order',)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data.update({
            'filters': {
                'tags': list(Clip.tags.most_common().values_list('name', flat=True).order_by('id')),
                'languages': list(Clip.languages.most_common().values_list('name', flat=True).order_by('id')),
                'formats': list(Clip.formats.most_common().values_list('name', flat=True).order_by('id')),
                'types': list(Clip.types.most_common().values_list('name', flat=True).order_by('id')),
            }
        })
        return response

class InfoPushViewSet(viewsets.ModelViewSet):
    queryset = InfoPush.objects.all()
    serializer_class = InfoPushSerializer
