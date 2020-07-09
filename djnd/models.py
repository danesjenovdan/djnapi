from django.db import models

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from translations.models import Translatable

class GenericTag(TagBase):
  tag_type = 'generic'

  class Meta:
    verbose_name = 'Generic tag'
    verbose_name_plural = 'Generic tags'

class TaggedGenericItem(GenericTaggedItemBase):
  tag = models.ForeignKey(GenericTag,
                          related_name='%(app_label)s_%(class)s_items',
                          on_delete=models.CASCADE)

class LanguageTag(TagBase):
  tag_type = 'language'

  class Meta:
    verbose_name = 'Language tag'
    verbose_name_plural = 'Language tags'

class TaggedLanguageItem(GenericTaggedItemBase):
  tag = models.ForeignKey(LanguageTag,
                          related_name='%(app_label)s_%(class)s_items',
                          on_delete=models.CASCADE)

class FormatTag(TagBase):
  tag_type = 'format'

  class Meta:
    verbose_name = 'Format tag'
    verbose_name_plural = 'Format tags'

class TaggedFormatItem(GenericTaggedItemBase):
  tag = models.ForeignKey(FormatTag,
                          related_name='%(app_label)s_%(class)s_items',
                          on_delete=models.CASCADE)

class TypeTag(TagBase):
  tag_type = 'type'

  class Meta:
    verbose_name = 'Type tag'
    verbose_name_plural = 'Type tags'

class TaggedTypeItem(GenericTaggedItemBase):
  tag = models.ForeignKey(TypeTag,
                          related_name='%(app_label)s_%(class)s_items',
                          on_delete=models.CASCADE)

# Create your models here.
class Video(Translatable):
  title = models.CharField(max_length=512)
  desc = models.TextField(blank=True, null=True, verbose_name='Description')
  url = models.URLField(blank=True, null=True, verbose_name='URL')
  date = models.DateField(blank=True, null=True)
  order = models.IntegerField(default=0, blank=False, null=False)
  image = models.FileField(upload_to='images/video/', blank=True)
  tags = TaggableManager(through=TaggedGenericItem, blank=True)

  class TranslatableMeta:
    fields = ['title', 'desc']

  class Meta:
    ordering = ['order']

  def __str__(self):
    return self.title

class Project(Translatable):
  title = models.CharField(max_length=512)
  desc = models.TextField(blank=True, null=True, verbose_name='Description')
  date = models.DateField(blank=True, null=True)
  order = models.IntegerField(default=0, blank=False, null=False)
  url = models.URLField(blank=True, null=True, verbose_name='URL')
  image = models.FileField(upload_to='images/project/', blank=True)
  tags = TaggableManager(through=TaggedGenericItem, blank=True)

  class TranslatableMeta:
    fields = ['title', 'desc']

  class Meta:
    ordering = ['order']

  def __str__(self):
    return self.title

class Clip(Translatable):
  title = models.CharField(max_length=512)
  desc = models.TextField(blank=True, null=True, verbose_name='Description')
  date = models.DateField(blank=True, null=True)
  order = models.IntegerField(default=0, blank=False, null=False)
  publisher = models.CharField(max_length=512)
  image = models.FileField(upload_to='images/clip/', blank=True)
  tags = TaggableManager(through=TaggedGenericItem, blank=True, verbose_name='(Generic) Tags')
  languages = TaggableManager(through=TaggedLanguageItem, blank=True, verbose_name='Language tags')
  formats = TaggableManager(through=TaggedFormatItem, blank=True, verbose_name='Format tags')
  types = TaggableManager(through=TaggedTypeItem, blank=True, verbose_name='Type tags')
  url = models.URLField(blank=True, null=True, verbose_name='URL')

  class TranslatableMeta:
    fields = ['title', 'desc']

  class Meta:
    ordering = ['order']

  def __str__(self):
    return self.title

# this is a singleton
class InfoPush(Translatable):
  title = models.CharField(max_length=512)
  desc = models.TextField(blank=True, null=True, verbose_name='Description')
  cta_text = models.CharField(max_length=512, verbose_name='Button text')
  cta_url = models.URLField(verbose_name='Button URL')
  visible = models.BooleanField(default=False)
  image = models.FileField(upload_to='images/infopush/', blank=True)

  class TranslatableMeta:
    fields = ['title', 'desc', 'cta_text', 'cta_url']

  class Meta:
    verbose_name = 'Info push'
    verbose_name_plural = 'Info pushes'

  def save(self, *args, **kwargs):
    self.pk = 1
    super(InfoPush, self).save(*args, **kwargs)

  def delete():
    pass

  @classmethod
  def load(cls):
    obj, created = cls.objects.get_or_create(pk=1)
    return obj

  def __str__(self):
    return self.title
