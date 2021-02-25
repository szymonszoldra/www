# Generated by Django 3.1.2 on 2020-11-20 13:29

from django.db import migrations
import common.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201030_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footersettings',
            name='content',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('header', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))])))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='footersettings',
            name='content_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('header', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))])))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='footersettings',
            name='content_pl',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('header', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))])))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='content',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('post_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['blog.PostIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))])), ('header', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))])))])), ('map', wagtail.core.blocks.StructBlock([('center_longitude', wagtail.core.blocks.FloatBlock()), ('center_latitude', wagtail.core.blocks.FloatBlock()), ('zoom', wagtail.core.blocks.FloatBlock()), ('bearing', wagtail.core.blocks.FloatBlock()), ('pitch', wagtail.core.blocks.FloatBlock()), ('markers', wagtail.core.blocks.ListBlock(common.blocks.MapMarker)), ('placeholder', wagtail.images.blocks.ImageChooserBlock(help_text='Insert a screenshot of the map here'))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='content_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('post_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['blog.PostIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))])), ('header', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))])))])), ('map', wagtail.core.blocks.StructBlock([('center_longitude', wagtail.core.blocks.FloatBlock()), ('center_latitude', wagtail.core.blocks.FloatBlock()), ('zoom', wagtail.core.blocks.FloatBlock()), ('bearing', wagtail.core.blocks.FloatBlock()), ('pitch', wagtail.core.blocks.FloatBlock()), ('markers', wagtail.core.blocks.ListBlock(common.blocks.MapMarker)), ('placeholder', wagtail.images.blocks.ImageChooserBlock(help_text='Insert a screenshot of the map here'))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='content_pl',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('post_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['blog.PostIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))])), ('header', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=200, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False))])))])), ('map', wagtail.core.blocks.StructBlock([('center_longitude', wagtail.core.blocks.FloatBlock()), ('center_latitude', wagtail.core.blocks.FloatBlock()), ('zoom', wagtail.core.blocks.FloatBlock()), ('bearing', wagtail.core.blocks.FloatBlock()), ('pitch', wagtail.core.blocks.FloatBlock()), ('markers', wagtail.core.blocks.ListBlock(common.blocks.MapMarker)), ('placeholder', wagtail.images.blocks.ImageChooserBlock(help_text='Insert a screenshot of the map here'))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
    ]
