#-*- coding: utf-8 -*-
import urllib
import urllib2

from config import *
import urllib,urllib2,cookielib

class Lover:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        cj = cookielib.LWPCookieJar()
        try:
            cj.revert('renren,cookie')
        except:
            pass 
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(self.opener)
        self.login()

    def login(self):
        params = {
            'email':self.username,
            'password':self.password,
            'domain': LOGIN_DOMAIN,
        }
        try:
            req = urllib2.Request(LOGIN_PAGE, urllib.urlencode(params))
            self.opener.open(req)
        except:
            raise "***Exception:Login Unvalid!"

    def do_action(self, url):
        params = { 'domain':LOVER_DOMAIN }
        try:
            req = urllib2.Request(url, urllib.urlencode(params))
            r   = self.opener.open(req).read()
            print r
        except:
            raise "***Exception:\n%s\n%s" % (url, r)

    def auto_care(self):
        for url in (SUN,SUN,WATER,WATER):
            self.do_action(url)
