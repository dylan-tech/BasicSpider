# coding:utf-8
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SpiderMan(object):
	def __init__(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()

	def crawl(self, root_url):
		# 添加入口URL
		self.manager.add_new_url(root_url)
		# 判断url管理器中是否有新的url，同时判断抓取了多少个url
		while (self.manager.has_new_url() and self.manager.old_url_size() < 30):
			try:
				# 从URL管理器获得新的url
				new_url = self.manager.get_new_url()
				# HTML下载器下载网页
				html = self.downloader.download(new_url)
				# HTML解析器抽取网页数据
				new_urls, data = self.parser.parser(new_url, html)
				# 将抽取的url添加到URL管理器中
				self.manager.add_new_urls(new_urls)
				# 数据存储器存储文件
				self.output.store_data(data)
				print "已经抓取%s个连接"%self.manager.old_url_size()
			except Exception, e:
				print "crawl failed"
		self.output.output_html()

if __name__ == "__main__":
	spider = SpiderMan()
	spider.crawl('https://baike.baidu.com/item/网络爬虫')

				
				
		
