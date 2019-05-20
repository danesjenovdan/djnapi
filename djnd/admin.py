from django.contrib import admin

from translations.admin import TranslatableAdmin, TranslationInline
from adminsortable2.admin import SortableAdminMixin

from djnd.models import Video, Project, Clip, InfoPush

# Register your models here.
class VideoAdmin(SortableAdminMixin, TranslatableAdmin):
  inlines = [TranslationInline,]

class ProjectAdmin(SortableAdminMixin, TranslatableAdmin):
  inlines = [TranslationInline,]

class ClipAdmin(SortableAdminMixin, TranslatableAdmin):
  inlines = [TranslationInline,]

class InfoPushAdmin(TranslatableAdmin):
  inlines = [TranslationInline,]

admin.site.register(Video, VideoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Clip, ClipAdmin)
admin.site.register(InfoPush, InfoPushAdmin)