#coding=utf8

from base import TaoBao


class CompaniesGet(TaoBao):
    data_name = 'logistics_companies'
    data_type = 'logistics_company'
    method = 'logistics.companies.get'
    fields= 'id,code,name'


class OfflineSent(TaoBao):
    data_name = 'shipping'
    data_type = 'shipping'
    method = 'logistics.offline.send'
    fields= 'is_success'
        
