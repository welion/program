#-*-coding : utf-8 -*-
#!/usr/bin/env python
import os.path

import tornado.auth
import tornado.escape
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
import pycurl
import os,sys

define("port", default=8000, help="run on the given port...", type=int)



def GetSiteStat(URL):
        c = pycurl.Curl()
        c.setopt(pycurl.URL, URL)
        c.setopt(pycurl.CONNECTTIMEOUT, 5)
        c.setopt(pycurl.TIMEOUT, 5)
        c.setopt(pycurl.NOPROGRESS, 1)    
        c.setopt(pycurl.FORBID_REUSE, 1) 
        c.setopt(pycurl.MAXREDIRS, 1)   
        c.setopt(pycurl.DNS_CACHE_TIMEOUT,30) 
        indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")  
        c.setopt(pycurl.WRITEHEADER, indexfile)  
        c.setopt(pycurl.WRITEDATA, indexfile)   
        try:
                c.perform()   
        except Exception,e:
                print "connecion error:"+str(e)
                c.close()
        NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME) 
        CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)    
        PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME) 
        STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
        TOTAL_TIME = c.getinfo(c.TOTAL_TIME)  
        HTTP_CODE =  c.getinfo(c.HTTP_CODE)  
        SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD) 
        HEADER_SIZE = c.getinfo(c.HEADER_SIZE)   
        SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)  

        return {"HTTP_CODE":HTTP_CODE,
                "NAMELOOKUP_TIME":NAMELOOKUP_TIME,
                "CONNECT_TIME":CONNECT_TIME,
                "PRETRANSFER_TIME":PRETRANSFER_TIME,
                "STARTTRANSFER_TIME":STARTTRANSFER_TIME,
                "TOTAL_TIME":TOTAL_TIME,
                "SIZE_DOWNLOAD":SIZE_DOWNLOAD,
                "HEADER_SIZE":HEADER_SIZE,
                "SPEED_DOWNLOAD":SPEED_DOWNLOAD}

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/",MainHandler),
			(r"/recommended",RecommendedHandler),
			(r"/discussion",DiscussionHandler),
			(r"/monitor", MonitorHandler),
		]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__),"templates"),
			static_path=os.path.join(os.path.dirname(__file__),"static"),
			ui_modules={"Book" : BookModule,
				    "Info" : InfoModule,
				},
			debug = True,
			)
		tornado.web.Application.__init__(self,handlers,**settings)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(
			"index.html",
			page_title = "Burt's Books | Home",
			header_text = "Welcome to Burt's Books!",
		)

class MonitorHandler(tornado.web.RequestHandler):
	def get(self):
		SiteInfo = GetSiteStat("http://www.baidu.com")
		information = {"HTTP_CODE":SiteInfo["HTTP_CODE"],
				"NAMELOOKUP_TIME":SiteInfo["NAMELOOKUP_TIME"],
				"CONNECT_TIME":SiteInfo["CONNECT_TIME"],
				"PRETRANSFER_TIME":SiteInfo["PRETRANSFER_TIME"],
				"STARTTRANSFER_TIME":SiteInfo["STARTTRANSFER_TIME"],
				"TOTAL_TIME":SiteInfo["TOTAL_TIME"],
				"SIZE_DOWNLOAD":SiteInfo["SIZE_DOWNLOAD"]
				}
		self.render("monitor.html",
			Info = infomation,
			)


class RecommendedHandler(tornado.web.RequestHandler):
	def get(self):

		books=[
			{
				"title":"Programming Collective Intelligence",
				"subtitle": "Building Smart Web 2.0 Applications",
				"image":"/static/images/collective_intelligence.gif",
				"author": "Toby Segaran",
				"date_added":1310248056,
				"date_released": "August 2007",
				"isbn":"978-0-596-52932-1",
				"description":"<p>This fascinating book demonstrates how you can build web applications to mine the enormous amount of data created by people on the Internet. With the sophisticated algorithms in this book, you can write smart programs to access interesting datasets from other web sites, collect data from users of your own applications, and analyze and understand the data once you've found it.</p>"
			},
			{
				"title":"RESTful Web Services",
				"subtitle": "Web services for the real world",
				"image":"/static/images/restful_web_services.gif",
				"author": "Leonard Richardson, Sam Ruby",
				"date_added":1311148056,
				"date_released": "May 2007",
				"isbn":"978-0-596-52926-0",

			},
			{
				"title":"Head First Python",
				"subtitle": "",
				"image":"/static/images/head_first_python.gif",
				"author": "Paul Barry",
				"date_added":1311348056,
				"date_released": "November 2010",
				"isbn":"Head First Python",
				"description":"<p>Ever wished you could learn Python from a book? Head First Python is a complete learning experience for Python that helps you learn the language through a unique method that goes beyond syntax and how-to manuals, helping you understand how to be a great Python programmer. You'll quickly learn the language's fundamentals, then move onto persistence, exception handling, web development, SQLite, data wrangling, and Google App Engine. You'll also learn how to write mobile apps for Android, all thanks to the power that Python gives you.</p>"
			}
		]

		self.render(
			"recommended.html",
			page_title = "Burt's Books | Recommended Reading",
			header_text = "Recommended Reading",
			books = books,
		)

class DiscussionHandler(tornado.web.RequestHandler):
        def get(self):
                self.render(
                        "discussion.html",
                        page_title = "Burt's Book | Discussion",
                        header_text = "Talkin' About Books With Burt",
                        comments=[
                        {
                                "user":"Alice",
                                "text": "I can't wait for the next version of Programming Collective Intelligence!"
                        },
                        {
                                "user":"Burt",
                                "text": "We can't either, Alice. In the meantime, be sure to check out RESTful Web Services too."
                        },
                        {
                                "user":"Melvin",
                                "text": "Totally hacked ur site lulz <script src=\"http://melvins-web-sploits.com/evil_sploit.js\"></script><script>alert('RUNNING EVIL H4CKS AND SPL0ITS NOW...');</script>"
                        }
                        ]
                )

class BookModule(tornado.web.UIModule):
        def render(self,book):
                return self.render_string(
                        "modules/book.html",
                        book = book
                )
        def css_file(self):
                return "css/recommended.css"

        def javascript_file(self):
                return "js/recommended.js"

class InfoModule(tornado.web.UIModule):
	def render(self,Info):
		return self.render_string(
			"module/Info.html",
			Info = Info
		)

def main():
        tornado.options.parse_command_line()
        http_server=tornado.httpserver.HTTPServer(Application())
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
        main()
		

