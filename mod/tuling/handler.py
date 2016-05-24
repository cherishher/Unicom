# -*- coding: utf-8 -*-
# @Date    : 2016/5/20  13:19
# @Author  : 490949611@qq.com

from config import *
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from collections import OrderedDict
import tornado.web
import tornado.gen
import json
import urllib

class TulingHandler(tornado.web.RequestHandler):

	def get(self):
		self.write('unicom web service')

	@tornado.web.asynchronous
	@tornado.gen.engine#没有的话，yield方法会报错！！！！boom~！
	def post(self):
		userinfo = self.get_argument('info',default=None)
		userid = self.get_argument('cardnum',default=-1)
		retjson = {'code':200, 'retinfo':''}
		if not userinfo:
			retjson['code'] = 408
			retjson['retinfo'] = 'params not enough'
		else:
			try:
				params = {
					'key': API_KEY,
                    'userid':userid,
					'info':userinfo.encode('utf-8')
				}
				client = AsyncHTTPClient()
				request = HTTPRequest(
                    TULING_URL,
					method='POST',
                    body=urllib.urlencode(params),#好像默认发的就是json呢2333
                    request_timeout=TIME_OUT)
				response = yield tornado.gen.Task(client.fetch,request)
				body = response.body
				retjson['retinfo'] = body
			except Exception,e:
				print str(e)#有问题时打印一下看看
				retjson['code'] = 500
				retjson['retinfo'] = 'error'
		self.write(json.dumps(retjson,ensure_ascii=False,indent=2))
		self.finish()