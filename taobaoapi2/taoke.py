#coding=utf8

from base import TaoBao

#淘客商品转换
class taobaokeItemsConvert(TaoBao):
    data_name = 'taobaoke_items'
    data_type = 'taobaoke_item'
    method = 'taobaoke.items.convert'
    fields = 'iid,title,nick,pic_url,price,click_url,commission,commission_rate,commission_num,commission_volume'


#淘客店铺转换
class taobaokeShopsConvert(TaoBao):
    data_name = 'taobaoke_shops'
    data_type = 'taobaoke_shop'
    method = 'taobaoke.shops.convert'
    fields = 'user_id,shop_title,click_url,shop_commission.rate'