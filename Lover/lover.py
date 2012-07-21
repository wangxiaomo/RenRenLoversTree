#-*- coding: utf-8 -*-
import urllib
import urllib2

from config import *

import re
import json
import urllib,urllib2,cookielib

class Lover:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.pid = None

        """ 如果有 renren.cookiejar 的话.复用登陆....貌似没成功过.FIX """
        cj = cookielib.LWPCookieJar()
        try:
            cj.revert('renren,cookie')
        except:
            pass 
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(self.opener)
        self.login()

    def _request_over_robots(self, url, bodies={}, headers={}):
        try:
            request = urllib2.Request(url, urllib.urlencode(bodies))
            request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0')
        except:
            raise Exception("Build Request Error")
        return self.opener.open(request)

    def login(self):
        params = {
            'email':self.username,
            'password':self.password,
            'domain': LOGIN_DOMAIN,
        }
        try:
            #req = urllib2.Request(LOGIN_PAGE, urllib.urlencode(params))
            #r = self.opener.open(req).read()
            r = self._request_over_robots(LOGIN_PAGE, params).read()
            try:
                pid = re.findall(r'http://lover.renren.com/(\d+)', r)[0]
            except:
                raise "***Exception:Pid Not Find."
            self.pid = pid
        except:
            raise "***Exception:Login Unvalid!"

    def do_action(self, url):
        params = { 'domain':LOVER_DOMAIN }
        try:
            #req = urllib2.Request(url, urllib.urlencode(params))
            #r   = self.opener.open(req).read()
            r = self._request_over_robots(url, params).read()
            print "%s %s" % (url, r)
        except Exception, e:
            raise "***Exception:\n%s\n%s" % (url, str(e))

    def auto_care(self):
        for url in (SUN,SUN,WATER,WATER):
            self.do_action(url+"?pid="+self.pid)
