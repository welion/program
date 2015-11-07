#-*-coding: utf-8 -*-

import pycurl
import os,sys

def GetSiteStat(URL):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, URL)
	c.setopt(pycurl.CONNECTTIMEOUT, 5)
	c.setopt(pycurl.TIMEOUT, 5)
	c.setopt(pycurl.NOPROGRESS, 1)    #屏蔽下载进度条  
	c.setopt(pycurl.FORBID_REUSE, 1)    #完成交互后强制断开连接，不重用  
	c.setopt(pycurl.MAXREDIRS, 1)    #指定HTTP重定向的最大数为1  
	c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)    #设置保存DNS信息的时间为30秒  
	indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")  
	c.setopt(pycurl.WRITEHEADER, indexfile)    #将返回的HTTP HEADER定向到indexfile文件对象  
	c.setopt(pycurl.WRITEDATA, indexfile)    #将返回的HTML内容定向到indexfile文件对象  
	try:
        	c.perform()    #提交请求  
	except Exception,e:
	       	print "connecion error:"+str(e)
        	c.close()
	NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)    #获取DNS解析时间  
	CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)    #获取建立连接时间  
	PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)    #获取从建立连接到准备传输所消  
	STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)    #获取从建立连接到传输开始消  
	TOTAL_TIME = c.getinfo(c.TOTAL_TIME)    #获取传输的总时间  
	HTTP_CODE =  c.getinfo(c.HTTP_CODE)    #获取HTTP状态码  
	SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)    #获取下载数据包大小  
	HEADER_SIZE = c.getinfo(c.HEADER_SIZE)    #获取HTTP头部大小  
	SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)    #获取平均下载速度

	return {"HTTP_CODE":HTTP_CODE,
		"NAMELOOKUP_TIME":NAMELOOKUP_TIME,
		"CONNECT_TIME":CONNECT_TIME,
		"PRETRANSFER_TIME":PRETRANSFER_TIME,
		"STARTTRANSFER_TIME":STARTTRANSFER_TIME,
		"TOTAL_TIME":TOTAL_TIME,
		"SIZE_DOWNLOAD":SIZE_DOWNLOAD,
		"HEADER_SIZE":HEADER_SIZE,
		"SPEED_DOWNLOAD":SPEED_DOWNLOAD}

if __name__=="__main__":
	info =  GetSiteStat("http://yangfuliu.website:8888")
	print info["HTTP_CODE"]
