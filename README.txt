  														_______________

																 README

														 Jichao Ouyang
														_______________


Table of Contents
_________________

1 install
2 configure
3 about API


Django Taobao
------------------------------------------------------------------------

a django plugin for [Taobao Open API]


[Taobao Open API] http://open.taobao.com


1 install
=========

  ,----
  | pip install django-taobao
  `----


2 configure
===========

  currently it's highly depand on [python-social-auth] for OAuth2
  authentication. so the only thing you need to do for authentication is
  open your django `settings.py' and add these variable:

  ,----
  | INSTALLED_APPS = (
  |     ...
  |     'django_taobao',
  |     'django_social_auth.apps.django_app.default',
  | )
  | 
  | AUTHENTICATION_BACKENDS = [
  |     'social.backends.taobao.TAOBAOAuth',
  | ]
  | 
  | SOCIAL_AUTH_TAOBAO_KEY = 'your client id'
  | SOCIAL_AUTH_TAOBAO_SECRET = 'your app secret'
  `----

  now modify your `urls.py'
  ,----
  | url(r'^taobao/', include('taobao.urls')), # this is taobao api example
  | url('', include('social.apps.django_app.urls', namespace='social')), # this is for auth
  `----
  now you can just visit `youhost.com/login/taobao' login and get the
  `token'


  [python-social-auth] https://github.com/omab/python-social-auth


3 about API
===========

  now with the token just got, you can use taobao api now.

  the get sold list example in `view' show how to use the api

  ,----
  | @login_required
  | def sold_items(request):
  |     user = get_object_or_404(UserSocialAuth.objects.filter(provider='taobao'),user=request.user)
  |     token = user.extra_data['access_token']
  |     sold = TradesSoldGet()
  |     sold.setParams(access_token=token)
  |     sold.fetch()
  |     return render_to_response("taobao/sold_items.html", RequestContext(request, {'items':sold.datas}))
  `----
