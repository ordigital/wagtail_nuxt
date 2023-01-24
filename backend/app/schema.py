from __future__ import unicode_literals
from django.db import models

import graphene
from graphene_django import DjangoObjectType
from app.models import NewsPage


class ArticleNode(DjangoObjectType):
    class Meta:
        model = NewsPage
        only_fields = ['id', 'title', 'date', 'intro', 'body']


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)

    @graphene.resolve_only_args
    def resolve_articles(self):
        return NewsPage.objects.live()

schema = graphene.Schema(query=Query)