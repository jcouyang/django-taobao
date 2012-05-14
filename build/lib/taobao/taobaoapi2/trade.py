#coding=utf8

from base import TaoBao

trade_fields = 'seller_nick, buyer_nick, title, type, created, tid, seller_rate, buyer_rate, status, payment, discount_fee, adjust_fee, post_fee, total_fee, pay_time, end_time, modified, consign_time, buyer_obtain_point_fee, point_fee, real_point_fee, received_payment, commission_fee, pic_path, num_iid, num, price, cod_fee, cod_status, shipping_type, receiver_name, receiver_state, receiver_city, receiver_district, receiver_address, receiver_zip, receiver_mobile, receiver_phone,seller_flag,alipay_id,alipay_no,is_lgtype,is_force_wlb,is_brand_sale,buyer_area,has_buyer_message,orders'
#搜索当前会话用户作为买家达成
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

class PostFeeUpdate(TaoBao):
    """docstring for PostFeeUpdate"""
    data_name= False    
    data_type='trade'
    method='trade.postage.update'
    fields="post_fee,total_fee,payment"
        