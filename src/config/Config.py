#!/usr/bin/env python
# -*- coding: utf-8 -*-
LOGIN_INFO={
    'APP_KEY' : '709226079',
    'APP_SECRET' : '4136ddf0aae8edf0b0752d07eae95654',
    'CALLBACK_URL': 'https://api.weibo.com/oauth2/default.html',
    'AUTH_URL' : 'https://api.weibo.com/oauth2/authorize',
    'USERID' : 'miggle_3@sina.com',
    'PASSWD' : 'APTX4869',
}

def get_sqlite_path():
    '''
    ##获取数据库路径
    *   win系统和Linux路径不同，做个判断，sina.db放在base_pat下
    '''
    if "win" in sys.platform:
        return get_base_path() + "\\" + "sina.db"
    else:
        return get_base_path() + "/" + "sina.db"
