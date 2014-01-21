#coding=utf8
import urllib,urllib2,time,md5,json
from django.conf import settings

TAOBAO_API_URL = settings.TAOBAO_API_URL

class TaoBao(object):
    def __init__(self):
        self.datas = ''
        self.p = dict(
            method = '',
            v = '2.0',
            format = 'json',
            fields = 'is_success',
        )
    def setParams(self,**kwargs):
        self.p.update(kwargs)
    def setFields(self,fields):
        self.p['fields'] = fields
    def setFormat(self,format):
        if format in ('json','xml'):self.p['format'] = format
    def fetch(self):
        form_data = urllib.urlencode(self.p)
        urlopen = urllib2.urlopen(TAOBAO_API_URL,form_data)
        print TAOBAO_API_URL+'?'+form_data
        rsp = urlopen.read()
        rsp = json.loads(rsp.decode('UTF-8'))
        if rsp.has_key('error_response'):
            return rsp['error_response']
        else:
            rsp = rsp[self.p['method'].replace('.','_').replace('taobao_','') + '_response']
            return rsp
