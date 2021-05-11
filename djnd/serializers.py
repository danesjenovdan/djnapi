from .models import Video, Clip, Project, InfoPush
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class VideoSerializer(TaggitSerializer, serializers.ModelSerializer):
  tags = TagListSerializerField()

  class Meta:
    model = Video
    fields = ('title', 'desc', 'alt', 'url', 'date', 'image', 'tags', 'order')

class ClipSerializer(TaggitSerializer, serializers.ModelSerializer):
  tags = TagListSerializerField()
  languages = TagListSerializerField()
  formats = TagListSerializerField()
  types = TagListSerializerField()

  class Meta:
    model = Clip
    fields = ('title', 'alt', 'desc', 'publisher', 'url', 'date', 'image', 'tags', 'languages', 'formats', 'types', 'order')

class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
  tags = TagListSerializerField()

  class Meta:
    model = Project
    fields = ('title', 'alt', 'desc', 'url', 'date', 'image', 'tags')

class InfoPushSerializer(TaggitSerializer, serializers.ModelSerializer):
  class Meta:
    model = InfoPush
    fields = ('title', 'desc', 'alt', 'cta_text', 'cta_url', 'visible', 'image')
