from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from webchat import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment'),
    url(r'^article/(?P<article_id>[0-9]+)/get_comment/$', views.get_comment, name='get_comment'),
    url(r'^(?P<column_id>[0-9]+)/$', views.column_page, name='column_page'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^webchat/$', views.webchat, name='webchat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)