from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from .api import api_router

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.urls import re_path
from search import views as search_views

# GraphQL
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

# Default url patterns
urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [

    # GraphQL API
    re_path(r'^api/graphql', csrf_exempt(GraphQLView.as_view())),
    re_path(r'^api/graphiql', csrf_exempt(GraphQLView.as_view(graphiql=True, pretty=True))),

    # API v2
    path('api/v2/', api_router.urls),

    # To read urls.py from subdir: 
    # path("pages/", include(wagtail_urls)),

    # General paths
    re_path(r'^', include(wagtail_urls)),
    path("", include(wagtail_urls)),

]


