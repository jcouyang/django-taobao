#coding=utf8

from base import TaoBao

items_fields = 'approve_status,iid,num_iid,title,nick,type,cid,pic_url,num,props,valid_thru,list_time,price,has_discount,has_invoice,has_warranty,has_showcase,modified,delist_time,postage_id,seller_cids,outer_id'

#搜索商品信息
class ItemsGet(TaoBao):
    data_name = 'items'
    data_type = 'item'
    method = 'items.get'
    fields = items_fields

#获取当前会话用户的所有商品列表
class ItemsAllGet(TaoBao):
    data_name = 'items'
    data_type = 'item'
    method = 'items.all.get'
    fields = items_fields

#得到当前会话用户出售中的商品列表
class ItemsOnsaleGet(TaoBao):
    data_name = 'items'
    data_type = 'item'
    method = 'items.onsale.get'
    fields = items_fields

#得到当前会话用户库存中的商品列表
class ItemsInventoryGet(TaoBao):
    data_name = 'items'
    data_type = 'item'
    method = 'items.inventory.get'
    fields = items_fields

#得到单个商品信息
class ItemGet(TaoBao):
    data_name = False
    data_type = 'item'
    method = 'items.inventory.get'
    fields = 'iid,detail_url,num_iid,title,nick,type,cid,seller_cids,props,input_pids,input_str,desc,pic_url,num,valid_thru,list_time,delist_time,stuff_status,location,price,post_fee,express_fee,ems_fee,has_discount,freight_payer,has_invoice,has_warranty,has_showcase,modified,approve_status,postage_id,auction_point,property_alias,item_img,prop_img,sku,outer_id,is_virtual,is_taobao,is_ex,videos,is_3D,score,volume,one_station'

#更新商品信息
class ItemUpdate(TaoBao):
    data_name = False
    data_type = 'item'
    method = 'items.inventory.get'
    fields = ''