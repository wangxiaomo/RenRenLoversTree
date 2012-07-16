#-*- coding: utf-8 -*-

"""
Common Config Of RenRen
"""

""" 登陆验证并采集 pid """
LOGIN_DOMAIN = "renren.com"
LOGIN_PAGE   = "http://www.renren.com/PLogin.do"

""" Lover 情侣空间. && 进行浇花等 Action """
LOVER_DOMAIN = "lover.renren.com"
LOVER_HOST   = "http://%s" % LOVER_DOMAIN
SUN          = "%s/app/tree/op/sunning" % LOVER_HOST
WATER        = "%s/app/tree/op/watering" % LOVER_HOST
