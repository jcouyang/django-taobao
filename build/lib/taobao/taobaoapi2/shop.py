#coding=utf8

from base import TaoBao

class ShopGet(TaoBao):
    data_name = False
    data_type = 'shop'
    method = 'shop.get'
    fields = 'sid,cid,nick,title,desc,bulletin,pic_path,created,modified'

class AddrSearch(TaoBao):
    data_name = 'addresses'
    data_type = 'address_result'
    method = 'logistics.address.search'
    fields = 'addr,area_id,cancel_def,city'

