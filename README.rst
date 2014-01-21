django taobao
========

a django plugin for `Taobao Open API <http://open.taobao.com>`_

install
--------

pip install django-taobao

configure
-------
currently it's highly depand on `python social auth <https://github.com/omab/python-social-auth>`_ for OAuth2
authentication. so the only thing you need to do for authentication is
open your django ``settings.py`` and add these variable::

  INSTALLED_APPS = (
      ...
      'django_taobao',
      'django_social_auth.apps.django_app.default',
  )
  
  AUTHENTICATION_BACKENDS = [
      'social.backends.taobao.TAOBAOAuth',
  ]
  
  SOCIAL_AUTH_TAOBAO_KEY = 'your client id'
  SOCIAL_AUTH_TAOBAO_SECRET = 'your app secret'
	TAOBAO_API_URL ='https://gw.api.tbsandbox.com/router/rest'

now modify your ``urls.py``::

  url(r'^taobao/', include('taobao.urls')), # this is taobao api example
  url('', include('social.apps.django_app.urls', namespace='social')), # this is for auth

now you can just visit ``youhost.com/login/taobao`` login and get the ``token``

how to use the API
-----------

now with the token just got, you can use taobao api now. 
the get user info example in ``view.py`` show how to use the api::
 
 def user_info(request):
           print request.user.id
           user = get_object_or_404(UserSocialAuth.objects.filter(provider='taobao'),user=request.user)
           token = user.extra_data['access_token']
           t = TaoBao()
           t.setParams(access_token=token, method='taobao.user.seller.get')
           t.setFields('nick,sex')
           return render_to_response("taobao/index.html", RequestContext(request, {'seller':t.fetch()}))


Contribute
----------
- Issue Tracker: https://github.com/jcouyang/django-taobao/issues
- Source Code: https://github.com/jcouyang/django-taobao
