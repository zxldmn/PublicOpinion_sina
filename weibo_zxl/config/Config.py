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

def get_base_path():
    '''
    ##获取当前环境根目录
    *   如果是通过scrapy crawl spider运行并访问该module，则在PATH中存在`系统目录/PolySpider/src`，我们只需要把该目录返回即可
    *   如果是通过web.py来访问该module,则并不保证该艮目存在，因此需要向path中添加该目录
    '''
    for p in sys.path:
        if 'PublicOpinion_sina' in p and 'src' in p and not 'web' in p:
            return p
    c_path = os.getcwd()
    base_path = c_path[:c_path.rfind("src")+3]
    sys.path.append(base_path)
    return base_path

def get_sqlite_path():
    '''
    ##获取数据库路径
    *   win系统和Linux路径不同，做个判断，app.db放在base_pat下
    '''
    if "win" in sys.platform:
        return get_base_path() + "\\" + "DB.db"
    else:
        return get_base_path() + "/" + "DB.db"


SHOW_SQL = False #True则会在控制台显示详细的SQL查询