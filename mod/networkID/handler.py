# -*- coding: utf-8 -*-
# @Date    : 2016/8/11  18:13
# @Author  : 490949611@qq.com



from tornado.httpclient import HTTPRequest, AsyncHTTPClient
import tornado.web
import tornado.gen
import json
from mod.models.networkID import networkID

class NetworkIDHandler(tornado.web.RequestHandler):

	@property
	def db(self):
		return self.application.db

	def get(self):
		self.write('unicom web service')

	@tornado.web.asynchronous
	@tornado.gen.engine#没有的话，yield方法会报错！！！！boom~！
	def post(self):
		userid = self.get_argument('cardnum',default=-1)
		retjson = {'code':200, 'retid':'null'}
		try:
			user = self.db.query(networkID).filter(networkID.useid == userid).first()
			if user == None:
				retjson = {'code':400,'retid':''}
			else:
				retjson = {'code':200,'retid':user.networkid}
		except Exception,e:
			print str(e)#有问题时打印一下看看
			retjson['code'] = 500
			retjson['retinfo'] = 'error'
		self.write(json.dumps(retjson,ensure_ascii=False,indent=2))
		self.finish()
