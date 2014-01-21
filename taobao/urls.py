from django.conf.urls import patterns, include, url

from taobao import views


urlpatterns = patterns('',
    url(r'^$', 'taobao.views.user_info', name='userinfo'),
)
