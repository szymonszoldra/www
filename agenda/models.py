from enum import Enum

from django.core.validators import RegexValidator
from django.db import models
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.embeds.models import Embed
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from common.models import SFIPage
from common.utils import paginate


@register_snippet
class Sponsor(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('name'))
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('logo')
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("sponsor")
        verbose_name_plural = _("sponsors")


class SpeakerIndex(SFIPage):
    subpage_types = ['Speaker']

    SPEAKERS_PER_PAGE = 10

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['speakers'] = paginate(
            Speaker.objects.live().public().descendant_of(self).order_by('title'),
            request, SpeakerIndex.SPEAKERS_PER_PAGE)
        return context

    class Meta:
        verbose_name = _('speakers index')
        verbose_name_plural = _('speakers indexes')


class Speaker(SFIPage):
    content = RichTextField(verbose_name=_('content'))
    sponsor = models.ForeignKey(Sponsor, null=True, blank=True, on_delete=models.PROTECT, verbose_name=_('sponsor'))

    content_panels = SFIPage.content_panels + [
        FieldPanel('content'),
        SnippetChooserPanel('sponsor'),
        InlinePanel('social_links', label='Social links')
    ]

    parent_page_types = ['SpeakerIndex']
    subpage_types = []

    class Meta:
        verbose_name = _('speaker')
        verbose_name_plural = _('speakers')


class SocialLinkTypes(models.TextChoices):
    FACEBOOK = 'facebook', 'Facebook'
    TWITTER = 'twitter', 'Twitter'
    GITHUB = 'github', 'Github'
    INSTAGRAM = 'instagram', 'Instagram'
    LINKEDIN = 'linkedin', 'Linkedin'
    EMAIL = 'email', _('Email')
    WEBSITE = 'site', _('Website')
    OTHER = 'other', _('Other')


class SocialLink(models.Model):
    speaker = ParentalKey(Speaker, on_delete=models.CASCADE, related_name='social_links')
    type = models.CharField(max_length=16, choices=SocialLinkTypes.choices, default=SocialLinkTypes.OTHER,
                            verbose_name=_('type'))
    link = models.URLField(max_length=512, verbose_name=_('link'))


class EditionIndex(SFIPage):
    subpage_types = ['Edition']

    EDITIONS_PER_PAGE = 10

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['editions'] = Edition.objects.live().public().descendant_of(self)
        return context

    class Meta:
        verbose_name = _('edition index')
        verbose_name_plural = _('edition indexes')


class Edition(SFIPage):
    start_date = models.DateTimeField(null=True, blank=True, verbose_name=_('edition start date'))
    end_date = models.DateTimeField(null=True, blank=True, verbose_name=_('edition end date'))

    content_panels = SFIPage.content_panels + [
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        InlinePanel('event_categories', label='Event categories')
    ]

    parent_page_types = ['EditionIndex']
    subpage_types = ['EventIndex']

    class Meta:
        verbose_name = _('edition')
        verbose_name_plural = _('editions')


class Category(models.Model):
    edition = ParentalKey(Edition, on_delete=models.CASCADE, related_name='event_categories', verbose_name=_('edition'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    icon = models.CharField(max_length=300, verbose_name=_('icon'))
    color = models.CharField(max_length=7,
                             default='#23211f',
                             validators=[RegexValidator(
                                 regex=r'^#([0-9a-fA-F]{6})$',
                                 message=_('Color must be in hex'),
                             ), ], verbose_name=_('color'))

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
        FieldPanel('color', widget=TextInput(attrs={'type': 'color', 'style': 'height:60'}))
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('event category')
        verbose_name_plural = _('event categories')


class EventIndex(SFIPage):
    parent_page_types = ['Edition']
    subpage_types = ['Event']

    color = models.CharField(max_length=7,
                             default='#23211f',
                             validators=[RegexValidator(
                                 regex=r'^#([0-9a-fA-F]{6})$',
                                 message=_('Color must be in hex'),
                             ), ], verbose_name=_('color'))

    content_panels = SFIPage.content_panels + [
        FieldPanel('color', widget=TextInput(attrs={'type': 'color', 'style': 'height:60'}))
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # TODO: display agenda block??
        return context

    class Meta:
        verbose_name = _('event list')
        verbose_name_plural = _('event lists')


class LanguageChoice(models.TextChoices):
    POLISH = 'pl', _('Polish')
    ENGLISH = 'en', _('English')


class Event(SFIPage):
    content = RichTextField(verbose_name=_('content'))
    date = models.DateTimeField(null=True, blank=True, verbose_name=_('date'))
    duration_minutes = models.IntegerField(null=True, blank=True, verbose_name=_('duration in minutes'))
    event_speaker = models.ForeignKey(Speaker, null=True, on_delete=models.PROTECT, verbose_name=_('speaker'))
    event_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL,
                                       verbose_name=_('category'))
    language = models.CharField(max_length=5, choices=LanguageChoice.choices, null=True, blank=True,
                                verbose_name=_('language'))
    sponsor = models.ForeignKey(Sponsor, null=True, blank=True, on_delete=models.PROTECT, verbose_name=_('sponsor'))
    recording = models.URLField(max_length=512, null=True, blank=True, verbose_name=_('link to recording'))

    class EventCategoryFieldPanel(FieldPanel):
        # Terrible hack to limit category choices to edition.
        def on_form_bound(self):
            edition_page = self.form.parent_page.get_parent().edition
            choices = edition_page.event_categories.all()
            self.form.fields['event_category'].queryset = choices
            super().on_form_bound()

    content_panels = SFIPage.content_panels + [
        FieldPanel('content'),
        FieldPanel('date'),
        FieldPanel('duration_minutes'),
        PageChooserPanel('event_speaker'),
        EventCategoryFieldPanel('event_category'),
        FieldPanel('language'),
        SnippetChooserPanel('sponsor'),
        FieldPanel('recording')
    ]

    parent_page_types = ['EventIndex']
    subpage_types = []

    @property
    def index(self):
        return self.get_parent()

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
