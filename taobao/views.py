# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from taobaoapi2 import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

from social_auth.models import UserSocialAuth
@login_required
def sold_items(request):

    user = get_object_or_404(UserSocialAuth.objects.filter(provider='taobao'),user=request.user)
    token = user.tokens['access_token']

    sold = TradesSoldGet()
    sold.setParams(access_token=token)
    sold.fetch()
    items = sold.datas
    return render_to_response("taobao/sold_items_mobile.html", RequestContext(request, {
		    'items':items,
                }))

@login_required
def mod_postfee(request):

    return_to = request.POST['next']
    user = get_object_or_404(UserSocialAuth.objects.filter(provider='taobao'),user=request.user)
    token = user.tokens['access_token']
    tid=request.POST['tid']
    post_fee=request.POST['postfee']
    post = PostFeeUpdate()
    post.setParams(access_token=token,tid=tid,post_fee=post_fee)
    post.fetch()
    
    if post.error_msg:
	    response = post.error_msg
    else:

        post.datas['tid']=tid
        response = json.dumps(post.datas)
        print response
    if "application/json" in request.META['HTTP_ACCEPT_ENCODING']:
        mimetype = 'application/json'
    else:
        mimetype = 'text/plain'
    return HttpResponse(response, mimetype=mimetype)

