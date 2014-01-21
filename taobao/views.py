# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from taobaoapi import *
from social.apps.django_app.default.models import UserSocialAuth

@login_required
def user_info(request):
    print request.user.id
    user = get_object_or_404(UserSocialAuth.objects.filter(provider='taobao'),user=request.user)
    token = user.extra_data['access_token']
    t = TaoBao()
    t.setParams(access_token=token, method='taobao.user.seller.get')
    t.setFields('nick,sex')
    return render_to_response("taobao/index.html", RequestContext(request, {'seller':t.fetch()}))
