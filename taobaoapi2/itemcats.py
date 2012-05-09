#coding=utf8

from base import TaoBao

class ShopcatsListGet(TaoBao):
    data_name = 'shop_cats'
    data_type = 'shop_cat'
    method = 'shopcats.list.get'
    fields = 'cid,parent_cid,name,is_parent'
