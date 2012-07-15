#-*- coding: utf-8 -*-

from Lover import Lover

accounts = [
    {'username':'15263142800', 'password':'xza2201367'},
    {'username':'13516227628', 'password':'lrq13516227628'},
]

for user in accounts:
    lover = Lover(user['username'], user['password'])
    lover.auto_care()
