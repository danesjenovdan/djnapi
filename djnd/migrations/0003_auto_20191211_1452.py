# Generated by Django 2.2.1 on 2019-12-11 14:52

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('djnd', '0002_auto_20190520_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clip',
            name='formats',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='djnd.TaggedFormatItem', to='djnd.FormatTag', verbose_name='Format tags'),
        ),
        migrations.AlterField(
            model_name='clip',
            name='languages',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='djnd.TaggedLanguageItem', to='djnd.LanguageTag', verbose_name='Language tags'),
        ),
        migrations.AlterField(
            model_name='clip',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='djnd.TaggedGenericItem', to='djnd.GenericTag', verbose_name='(Generic) Tags'),
        ),
        migrations.AlterField(
            model_name='clip',
            name='types',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='djnd.TaggedTypeItem', to='djnd.TypeTag', verbose_name='Type tags'),
        ),
    ]
