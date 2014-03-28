#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from src.util import SqliteUtil
def save_weibo_info(weibo_info_lists):
	SqliteUtil.checkTableExist()
	sql="insert into weibo_info (text,created_data,reposts_count,comments_count,attitudes_count) values (?,?,?,?,?)"
	SqliteUtil.execute_sql(sql,weibo_info_lists)
	return "success"
