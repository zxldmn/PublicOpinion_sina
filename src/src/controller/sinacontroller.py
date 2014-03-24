#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
from src.util import Access_token
from weibo import APIClient
urls = (
    '/user_show/(.*)','GetUserShow',
    '/public_timeline/(.*)','GetPublic'
    #'/get_app_by_app_name', 'GetAppByAppName',
    #'/get_app_by_app_id', 'GetAppByAppId',
    #'/get_app_count', 'GetAppCount',
    #'/app_list/(.*)','AppList',
    # '/get_app_list','GetAppList',
    # '/get_app_list_by_default', 'GetAppListByDefault',
    # '/get_app_list_by_platform/(.*)','GetAppListByPlatform',
    # '/get_app_list_by_category/(.*)','GetAppListByCategory',
    #'/category_statistic', 'CategoryStatistic',
    #'/platform_statistic', 'PlatformStatistic',
    #'/update_category/(.*)/(.*)', 'UpdateCategory',    
)
class GetUserShow:
    def GET(self,uid_info):
        client=Access_token.get_client()
        r = client.users.show.get(uid=uid_info)
        return json.dumps(r)
class GetPublic:
    def GET(self,count):
        client = Access_token.get_client()
        r = client.statuses.public_timeline.get(count = 2)
        #a = json.dumps(r['statuses'])
        print type(r['statuses'])
        print type(r['statuses'][0])
        return json.dumps(r['statuses'][*]['created_at'])










#class GetAppByAppName:
#    def GET(self):
#        paras = StringUtil.convert_query_to_paras(web.ctx.query)
#        app_name = paras['app_name']
#
#        app = AppDao.get_app_by_app_name(app_name)
#        return json.dumps(app)
#
#class GetAppByAppId:
#	def GET(self):
#		paras = StringUtil.convert_query_to_paras(web.ctx.query)
#		app_id = paras['app_id']
#		app = AppDao.get_app_by_app_id(app_id)
#		return json.dumps(app)
#
#class GetAppCount:
#	def GET(self):
#		count = AppDao.get_app_count()
#		return json.dumps([{'count':count}])
#
#class CategoryStatistic:
#	def GET(self):
#                categorys=AppDao.category_statistic()
#                result = '['
#                for i in categorys:
#                    if i == '3600':
#                        result += "{name:'" + str(CategoryUtil.get_category_name_by_id(i)) + "',y:" + str(categorys[i]) + ",sliced: true, selected: true},"
#                    else:
#                        result += "['"+ str(CategoryUtil.get_category_name_by_id(i)) + "'," + str(categorys[i])+ "],"
#                result=result[:-1] + ']'
#		return result
#
#class PlatformStatistic:
#    def GET(self):
#        platforms = AppDao.platform_statistic()
#        result = '['
#        for platform in platforms:
#            if platform == 'googleplay':
#                result += "{name:'" + platform + "',y:" + str(platforms[platform]) + ",sliced: true, selected: true},"
#            else:
#                result += "['" + platform + "'," + str(platforms[platform]) + '],'
#        result=result[:-1] + ']'
#        return result
#
#class AppList:
#	def GET(self,page_index):
#                paras = StringUtil.convert_query_to_paras(web.ctx.query)
#                data = paras['data'].split(':')
#                if data[0]=='category':
#                    page_index = int(page_index)
#                    if page_index == 1:
#                            app_list = AppDao.get_app_list_by_categroy(data[1], row_number=500)
#                    else:
#                            app_list = AppDao.get_app_list_by_categroy(data[1], page_index=page_index, row_number=5000)
#                else:
#                    page_index = int(page_index)
#                    if data[1] == 'total':
#                        if page_index == 1:
#                                app_list = AppDao.app_list(row_number=500)
#                        else:
#                                app_list = AppDao.app_list(page_index=page_index, row_number=5000)
#                    else:
#                        if page_index == 1:
#                                app_list = AppDao.get_app_list_by_platform(data[1], row_number=500)
#                        else:
#                                app_list = AppDao.get_app_list_by_platform(data[1], page_index=page_index, row_number=5000)
#                                
#                return json.dumps({'aaData':app_list})
#
#class GetAppListByPlatform:
#	def GET(self,platform):
#		app_list = AppDao.get_app_list_by_platform(platform)
#		return json.dumps({'aaData':AppDao.get_app_list_by_platform(platform)})
#            
#class GetAppListByCategory:
#	def GET(self,categroy):
#		app_list = AppDao.get_app_list_by_categroy(categroy)
#		return json.dumps({'aaData':AppDao.get_app_list_by_categroy(categroy)})
#class UpdateCategory:
#	def GET(self,app_id,categroy_name):
#                AppDao.update_category(int(app_id),categroy_name)
#		return 'success'
#
## class GetAppList:
## 	def GET(self):
## 		paras = StringUtil.convert_query_to_paras(web.ctx.query)
## 		aoData = paras['aoData']
## 		aoData = StringUtil.aoData_map_convert(aoData)
## 		print aoData
## 		iColumns = aoData['iColumns'] #列数
## 		iDisplayLength = aoData['iDisplayLength'] #展示的行数
## 		iDisplayStart = aoData['iDisplayStart'] #起始页数
## 		page_index = iDisplayStart / iDisplayLength + 1
## 		print page_index
## 		app_list = AppDao.get_app_list(page_index=page_index, row_number=iDisplayLength)
## 		iTotalRecords = AppDao.get_app_count()
## 		iTotalDisplayRecords = iTotalRecords
#
## 		return json.dumps({
## 			'aaData':app_list,
## 			'iTotalRecords':iTotalRecords,
## 			'iTotalDisplayRecords':iTotalDisplayRecords,
## 			'sEcho':aoData['sEcho']})
## 		# return '{"sEcho":1,"iTotalRecords":67,"iTotalDisplayRecords":67,"aaData": [["QQ", "com.tencent.mobileqq", "\u901a\u8baf", "<a href=\'baidu.com\'>1</a>"]]}'
#
## class GetAppListByDefault:
## 	def GET(self):
## 		app_list = AppDao.get_app_list(row_number = 5000)
## 		iTotalRecords = AppDao.get_app_count()
## 		iTotalDisplayRecords = iTotalRecords
## 		return json.dumps({'aaData':app_list,})

sina_test= web.application(urls, locals())
