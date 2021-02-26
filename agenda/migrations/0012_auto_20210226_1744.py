# Generated by Django 3.1.4 on 2021-02-26 16:44

import common.blocks
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20210225_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventindex',
            name='reversed_order',
            field=models.BooleanField(default=False, verbose_name='reversed index order'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='content',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('event_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['agenda.EventIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))])), ('event_schedule', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['agenda.EventIndex', 'agenda.Edition']))])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=64, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=260, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False)), ('white_background', wagtail.core.blocks.BooleanBlock(default=False, required=False))])))])), ('map', wagtail.core.blocks.StructBlock([('center_longitude', wagtail.core.blocks.FloatBlock()), ('center_latitude', wagtail.core.blocks.FloatBlock()), ('zoom', wagtail.core.blocks.FloatBlock()), ('bearing', wagtail.core.blocks.FloatBlock()), ('pitch', wagtail.core.blocks.FloatBlock()), ('markers', wagtail.core.blocks.ListBlock(common.blocks.MapMarker)), ('placeholder', wagtail.images.blocks.ImageChooserBlock(help_text='Insert a screenshot of the map here'))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='content_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('event_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['agenda.EventIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))])), ('event_schedule', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['agenda.EventIndex', 'agenda.Edition']))])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=64, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=260, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False)), ('white_background', wagtail.core.blocks.BooleanBlock(default=False, required=False))])))])), ('map', wagtail.core.blocks.StructBlock([('center_longitude', wagtail.core.blocks.FloatBlock()), ('center_latitude', wagtail.core.blocks.FloatBlock()), ('zoom', wagtail.core.blocks.FloatBlock()), ('bearing', wagtail.core.blocks.FloatBlock()), ('pitch', wagtail.core.blocks.FloatBlock()), ('markers', wagtail.core.blocks.ListBlock(common.blocks.MapMarker)), ('placeholder', wagtail.images.blocks.ImageChooserBlock(help_text='Insert a screenshot of the map here'))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='content_pl',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('event_index', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['agenda.EventIndex'])), ('shown_posts', wagtail.core.blocks.IntegerBlock(min_value=1))])), ('event_schedule', wagtail.core.blocks.StructBlock([('index', wagtail.core.blocks.PageChooserBlock(page_type=['agenda.EventIndex', 'agenda.Edition']))])), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=64, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=260, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False)), ('white_background', wagtail.core.blocks.BooleanBlock(default=False, required=False))])))])), ('map', wagtail.core.blocks.StructBlock([('center_longitude', wagtail.core.blocks.FloatBlock()), ('center_latitude', wagtail.core.blocks.FloatBlock()), ('zoom', wagtail.core.blocks.FloatBlock()), ('bearing', wagtail.core.blocks.FloatBlock()), ('pitch', wagtail.core.blocks.FloatBlock()), ('markers', wagtail.core.blocks.ListBlock(common.blocks.MapMarker)), ('placeholder', wagtail.images.blocks.ImageChooserBlock(help_text='Insert a screenshot of the map here'))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='edition_footer',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=64, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=260, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False)), ('white_background', wagtail.core.blocks.BooleanBlock(default=False, required=False))])))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='edition footer'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='edition_footer_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=64, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=260, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False)), ('white_background', wagtail.core.blocks.BooleanBlock(default=False, required=False))])))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='edition footer'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='edition_footer_pl',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('section_title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('section_divider', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock())])), ('dropdown', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.RichTextBlock())])), ('photo_gallery', wagtail.core.blocks.StructBlock([('image_height', wagtail.core.blocks.IntegerBlock(default=64, max_value=2000, min_value=0)), ('image_width', wagtail.core.blocks.IntegerBlock(default=260, max_value=2000, min_value=0)), ('crop_to_fit', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('photos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.URLBlock(required=False)), ('white_background', wagtail.core.blocks.BooleanBlock(default=False, required=False))])))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True, verbose_name='edition footer'),
        ),
    ]
