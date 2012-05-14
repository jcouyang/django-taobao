#coding=utf8

from base import TaoBao

class UserGet(TaoBao):
    data_name = False
    data_type = 'user'
    method = 'user.get'
    fields = 'user_id,nick,sex,buyer_credit,seller_credit,location.city,location.state,location.country,created,last_visit,location.zip,birthday,type,has_more_pic,item_img_num,item_img_size,prop_img_num,prop_img_size,auto_repost,promoted_type,status,alipay_bind,consumer_protection'