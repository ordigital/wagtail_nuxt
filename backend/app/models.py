from django.db import models
from wagtail.api import APIField

# Create your models here.

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class NewsPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full") 
    ]

    api_fields = [
        APIField('date'),
        APIField('intro'),
        APIField('body')
    ]
    

    