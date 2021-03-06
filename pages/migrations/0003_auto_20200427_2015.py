# Generated by Django 3.0.5 on 2020-04-27 18:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200427_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('post_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['blog.PostIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))]))]),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='content_en',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('post_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['blog.PostIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))]))], null=True),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='content_pl',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('post_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['blog.PostIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))]))], null=True),
        ),
    ]
