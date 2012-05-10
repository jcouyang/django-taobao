from django.conf.urls.defaults import *

from taobao import views


urlpatterns = patterns('',
    # offer
    url(r'^$', 'taobao.views.sold_items', name='sold_items'),
    
    # ajax validation
    #(r'^validate/$', 'ajax_validation.views.validate', {'form_class': BlogForm, 'callback': lambda request, *args, **kwargs: {'user': request.user}}, 'blog_form_validate'),
)
