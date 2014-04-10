#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import sqlite3

def check_sql(sql):
    '''
    检查sql语句是否为空
    '''
    if not sql or sql == '': 
        print('the [{}] is empty or equal None!'.format(sql))
        return False
    else: return True
def is_table_exist(table_name):
    '''
    检查table_name的数据库表是否存在
    '''
    con = sqlite3.connect("DB.db")
    return True if con.cursor().execute("SELECT count(*) FROM sqlite_master WHERE type= 'table' and name = ? ",(table_name,)).fetchone()[0] > 0 else False
# def checkTableExist():
#     '''
#     检查数据库中是否存在表
#     如果数据库中无ps_app, ps_app_detail和ps_status表，则创建表
#     '''
#     if not is_table_exist('weibo_info'):
#         sql_table_create = '''
#             CREATE TABLE weibo_info(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 text TEXT,
#                 created_data TEXT,
#                 reposts_count INTEGER,
#                 comments_count INTEGER,
#                 attitudes_count INTEGER
#             );
#         '''
#         create_table(sql_table_create)
#     if not is_table_exist('user_info'):
#         sql_table_create = '''
#             CREATE TABLE user_info(
#                 user_id INTEGER,
#                 screen_name TEXT,
#                 city_name TEXT,
#                 followers_count INTEGER,
#                 friends_count INTEGER,
#                 statuses_count INTEGER,
#             );
#         '''
#         create_table(sql_table_create)

def close_all(con):
    '''
    关闭数据库游标对象和数据库连接对象
    '''
    try:
        if not con.cursor(): con.cursor().close()
    finally:
        if con: con.close()
def execute_sql(sql, data = ""):
    '''
    执行sql语句
    data默认为空,data为list，可执行多条数据操作
    '''
    con = sqlite3.connect("DB.db")
    if not check_sql(sql): return
    cur = con.cursor()
    if data == "":
        cur.execute(sql)
    else:
        for d in data:
            
            cur.execute(sql, d)
    con.commit()
    close_all(con)
def create_table(sql):
    '''
    创建数据库表
    '''
    execute_sql(sql)
    print('Create Database Table Success!')
# def drop_table(table):
#     '''
#     如果表存在,则删除表，如果表中存在数据的时候，使用该方法的时候要慎用！
#     '''
#     if table is not None and table != '':
#         sql = 'DROP TABLE IF EXISTS ' + table
#         execute_sql(sql)
#     else:
#         print('the [{}] is empty or equal None!'.format(sql))
def save(sql, data):
    '''
    插入数据
    data为要插入的数据，格式为list，可以存放多条数据
    '''
    if not data: return
    execute_sql(sql, data)
    print('Insert Data Success!')
# def save_return_id(sql, data):
#     '''
#     插入数据
#     data为要插入的数据
#     返回插入生成的id，要求id为INTEGER PRIMARY KEY AUTOINCREMENT格式
#     '''
#     id = 0
#     if not data: return
#     con = sqlite3.connect(/Users/zhangxiaolin/Documents)
#     if not check_sql(sql): return
#     cur = con.cursor()
#     if Config.SHOW_SQL: print('process sql:[{}],paras:[{}]'.format(sql, d))
#     cur.execute(sql, data)
#     id = cur.lastrowid
#     con.commit()
#     close_all(con)
#     print "save_return_id :%d" %id 
#     return id
def update(sql, data):
    '''
    更新数据
    data为要插入的数据，格式为list，可以存放多条数据    
    '''
    if not data: return
    execute_sql(sql, data)
    print('Update Data Success!')
def delete(sql, data):
    '''
    删除数据
    '''
    if not data: return
    execute_sql(sql, data)
    print('Delete Data Success!')  





def checkTableExist():
    '''
    检查数据库中是否存在表

    '''
    if not is_table_exist('weibo_info'):
        sql_table_create = '''
            CREATE TABLE weibo_info(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                created_data TEXT,
                reposts_count INTEGER,
                comments_count INTEGER,
                attitudes_count INTEGER
            );
        '''
        create_table(sql_table_create)
    if not is_table_exist('user_info'):
        sql_table_create = '''
            CREATE TABLE user_info(
                user_id INTEGER,
                screen_name TEXT,
                city_name TEXT,
                followers_count INTEGER,
                friends_count INTEGER,
                statuses_count INTEGER
            );
        '''
        create_table(sql_table_create)


