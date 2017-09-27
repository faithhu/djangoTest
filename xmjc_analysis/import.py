#!/user/bin/env python
#coding:utf-8

from django.core import serializers
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmjc_analysis.settings")

if django.VERSION >=(1, 7):
    django.setup()

def main():
    from analysis.models import User
    f = open('./name.txt', encoding='utf-8')
    for line in f:
        name, pwd, email, _type = line.split('|')
        User.objects.create(username=name, userpass=pwd, useremail=email, usertype=_type)
    f.close()

def jsondb():
    from analysis.models import User
    data = eval(serializers.serialze("json", User.obejcts.all()))
    userdata = json.dumps(data)
    print(type(userdata))

if __name__ =="__main__":
    main()
    print("Success!")
