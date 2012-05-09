#coding=utf8

from base import TaoBao

trade_fields = 'seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,status,payment,discount_fee,adjust_fee,post_fee,pay_time,end_time,consign_time,modified,buyer_obtain_point_fee,point_fee,real_point_fee,received_payment,pic_path,iid,num,price,cod_fee,shipping_type,orders'

#搜索当前会话用户作为买家达成的
class TradesBoughtGet(TaoBao):
    data_name = 'trades'
    data_type = 'trade'
    method = 'trades.bought.get'
    fields = trade_fields


#搜索当前会话用户作为卖家已卖出
class TradesSoldGet(TaoBao):
    data_name = 'trades'
    data_type = 'trade'
    method = 'trades.sold.get'
    fields = trade_fields


class TradeGet(TaoBao):
    data_name = False
    data_type = 'trade'
    method = 'trade.get'
    fields = 'payment,seller_nick,buyer_nick,buyer_rate,stauts'

