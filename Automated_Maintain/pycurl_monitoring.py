#-*- coding: utf-8 -*-
#A python program for motoring the service quality

import os,sys
import time
import pycurl

URL=""	#����URL
c = pycurl.Curl() #����CURL����
c.setopt(pycurl.URL, URL) #���������url
c.setopt(pycurl.CONNECTTIMEOUT, 5) #���ӳ�ʱʱ��
c.setopt(pycurl.TIMEOUT, 5) #����ʱʱ��
c.setopt(pycurl.NOPROGRESS, 1) #�ر����ؽ�����
c.setopt(pycurl.FORBID_REUSE, 1) #��ɽ�����ǿ�ƶϿ���������
c.setopt(pycurl.MAXREDIRS, 1) #ָ��HTTP�ض���������
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30) #���ñ���DNS��Ϣ��ʱ��Ϊ30s# -*- coding: utf-8 -*-  
import os,sys  
import time  
import sys  
import pycurl  
 
URL="http://yangfuliu.website:8888"    #̽���Ŀ��URL  
c = pycurl.Curl()    #����һ��Curl����  
c.setopt(pycurl.URL, URL)    #���������URL����  
c.setopt(pycurl.CONNECTTIMEOUT, 5)    #�����������ӵĵȴ�ʱ��  
c.setopt(pycurl.TIMEOUT, 5)    #��������ʱʱ��  
c.setopt(pycurl.NOPROGRESS, 1)    #�������ؽ�����  
c.setopt(pycurl.FORBID_REUSE, 1)    #��ɽ�����ǿ�ƶϿ����ӣ�������  
c.setopt(pycurl.MAXREDIRS, 1)    #ָ��HTTP�ض���������Ϊ1  
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)    #���ñ���DNS��Ϣ��ʱ��Ϊ30��  
#����һ���ļ������ԡ�wb����ʽ�򿪣������洢���ص�httpͷ����ҳ������  
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")  
c.setopt(pycurl.WRITEHEADER, indexfile)    #�����ص�HTTP HEADER����indexfile�ļ�����  
c.setopt(pycurl.WRITEDATA, indexfile)    #�����ص�HTML���ݶ���indexfile�ļ�����  
try:  
    c.perform()    #�ύ����  
except Exception,e:  
    print "connecion error:"+str(e)  
    indexfile.close()  
    c.close()  
sys.exit()  
 
NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)    #��ȡDNS����ʱ��  
CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)    #��ȡ��������ʱ��  
PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)    #��ȡ�ӽ������ӵ�׼����������  
                                                      #�ĵ�ʱ��  
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)    #��ȡ�ӽ������ӵ����俪ʼ��  
                                                        #�ĵ�ʱ��  
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)    #��ȡ�������ʱ��  
HTTP_CODE =  c.getinfo(c.HTTP_CODE)    #��ȡHTTP״̬��  
SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)    #��ȡ�������ݰ���С  
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)    #��ȡHTTPͷ����С  
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)    #��ȡƽ�������ٶ�  
#��ӡ����������  
print "HTTP״̬�룺%s" %(HTTP_CODE)  
print "DNS����ʱ�䣺%.2f ms"%(NAMELOOKUP_TIME*1000)  
print "��������ʱ�䣺%.2f ms" %(CONNECT_TIME*1000)  
print "׼������ʱ�䣺%.2f ms" %(PRETRANSFER_TIME*1000)  
print "���俪ʼʱ�䣺%.2f ms" %(STARTTRANSFER_TIME*1000)  
print "���������ʱ�䣺%.2f ms" %(TOTAL_TIME*1000)  
print "�������ݰ���С��%d bytes/s" %(SIZE_DOWNLOAD)  
print "HTTPͷ����С��%d byte" %(HEADER_SIZE)  
print "ƽ�������ٶȣ�%d bytes/s" %(SPEED_DOWNLOAD)  
#�ر��ļ���Curl����  
indexfile.close()  
c.close() 

