import urllib2,urllib
from urllib2 import Request, urlopen, HTTPError
from urllib import urlencode
from urlparse import urlsplit
from social_auth.backends.exceptions import StopPipeline, AuthException, \
                                            AuthFailed, AuthCanceled, \
                                            AuthUnknownError, AuthTokenError, \
                                            AuthMissingParameter
from django.conf import settings
from django.utils import simplejson
import json
from django.contrib.auth import authenticate
from social_auth.backends import BaseOAuth2, OAuthBackend, USERNAME
# taobao OAuth base configuration
TAOBAO_OAUTH_HOST = 'oauth.taobao.com'
# TAOBAO_OAUTH_ROOT = 'authorize'
#Always use secure connection
TAOBAO_OAUTH_REQUEST_TOKEN_URL = 'https://%s/%s/request_token' % (TAOBAO_OAUTH_HOST)
TAOBAO_OAUTH_AUTHORIZATION_URL = 'https://%s/%s/authorize' % (TAOBAO_OAUTH_HOST)
TAOBAO_OAUTH_ACCESS_TOKEN_URL = 'https://%s/%s/token' % (TAOBAO_OAUTH_HOST)

TAOBAO_CHECK_AUTH = 'https://%s/oauth2.0/me' % TAOBAO_OAUTH_HOST
TAOBAO_USER_SHOW = 'https://%s/user/get_user_info' % TAOBAO_OAUTH_HOST
class TAOBAOBackend(OAuthBackend):
    """Weibo OAuth authentication backend"""
    name = 'taobao'
    # EXTRA_DATA = [('profile_image_url','avatar_url'), ('id','id')]
    # def get_user_id(self, details, response):
    #     print 'get user id',response
    #     return response['openid']
    
    # def get_user_details(self, response):
    #     """Return user details from Weibo account"""
    #     print response
    #     username = response['nickname']
    #     return {USERNAME: username,
    #             'email': '',  # not supplied
    #             'fullname': username,
    #             'first_name': username,
    #             'last_name': ''}
        
class TAOBAOAuth(BaseOAuth2):
    """Weibo OAuth authentication mechanism"""
    AUTHORIZATION_URL = TAOBAO_OAUTH_AUTHORIZATION_URL
    REQUEST_TOKEN_URL = TAOBAO_OAUTH_REQUEST_TOKEN_URL
    ACCESS_TOKEN_URL = TAOBAO_OAUTH_ACCESS_TOKEN_URL
    SERVER_URL = TAOBAO_OAUTH_HOST
    AUTH_BACKEND = TAOBAOBackend
    SETTINGS_KEY_NAME = 'TAOBAO_CONSUMER_KEY'
    SETTINGS_SECRET_NAME = 'TAOBAO_CONSUMER_SECRET'
   
    def user_data(self, access_token):
        """Return user data provided"""
        # params = {'access_token': access_token}
        
        # url = 'http://gw.api.tbsandbox.com/router/rest?' + urllib.urlencode(params)
        # # print url
        # response = urllib2.urlopen(url).read()
        # res = response.replace('callback(','')
        # res=res.replace(');','')
        # # print res
        # key,secr=self.get_key_and_secret()
        # response = json.loads(res)
        # params['openid']=response['openid']
        # params['oauth_consumer_key']=key
        # params['client_id']=response['client_id']
        # params['format']='json'
        # # print TAOBAO_USER_SHOW + '?' + urllib.urlencode(params)
        # response =urllib2.urlopen(TAOBAO_USER_SHOW + '?' + urllib.urlencode(params))
        # resuser = simplejson.load(response)
        # resuser.update(params)
        # # print 'resuser', resuser
        # try:
        #     return resuser
        # except ValueError:
        #     return None
        # request = self.oauth_request(access_token, TAOBAO_CHECK_AUTH)
        # json = self.fetch_response(request)
        # try:
        #     return simplejson.loads(json)
        # except ValueError:
        #     return None
    # def auth_complete(self, *args, **kwargs):
    #     """Completes loging process, must return user instance"""
    #     if self.data.get('error'):
    #         error = self.data.get('error_description') or self.data['error']
    #         raise AuthFailed(self, error)

    #     client_id, client_secret = self.get_key_and_secret()
    #     params = {'grant_type': 'authorization_code',  # request auth code
    #               'code': self.data.get('code', ''),  # server response code
    #               'client_id': client_id,
    #               'client_secret': client_secret,
    #               'redirect_uri': self.redirect_uri}
    #     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #     request = Request(self.ACCESS_TOKEN_URL, data=urlencode(params),
    #                       headers=headers)

    #     try:
    #         # print params
    #         res = urlopen(request).read()
    #         rslist = res.split('&')
    #         rsdict={}
        #     for rs in rslist:
        #         key,val = rs.split('=')
        #         if key == 'error':
        #             print 'error'
        #         else:
        #             rsdict[key]=val
        #     # print rsdict
        #     response = rsdict
        #     # response = simplejson.loads(rsdict)
        #     # print response
        # except HTTPError, e:
        #     # print e
        #     if e.code == 400:
        #         raise AuthCanceled(self)
        #     else:
        #         raise
        # except (ValueError, KeyError):
        #     raise AuthUnknownError(self)

        # if response.get('error'):
        #     error = response.get('error_description') or response.get('error')
        #     raise AuthFailed(self, error)
        # else:
        #     response.update(self.user_data(response['access_token']) or {})
        #     kwargs.update({
        #         'auth': self,
        #         'response': response,
        #         self.AUTH_BACKEND.name: True
        #     })
        #     return authenticate(*args, **kwargs)

# Backend definition
BACKENDS = {
    'taobao': TAOBAOAuth,
}
