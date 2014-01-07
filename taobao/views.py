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
from social.apps.django_app.default.models import UserSocialAuth

@login_required
def sold_items(request):

    user = get_object_or_404(UserSocialAuth.objects.filter(provider='taobao'),user=request.user)
    token = user.extra_data['access_token']
    sold = TradesSoldGet()
    sold.setParams(access_token=token)
    sold.fetch()
    items = sold.datas
    return render_to_response("taobao/sold_items.html", RequestContext(request, {'items':items}))

