from django.conf.urls import patterns, include, url

from taobao import views


urlpatterns = patterns('',
    url(r'^$', 'taobao.views.sold_items', name='solditems'),
)
