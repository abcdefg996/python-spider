# coding:utf8
from bs4 import BeautifulSoup
import re
# import parse
from urllib.parse import urljoin
class HtmlParser (object):
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		links =soup.find_all('a',href=re.compile(r"/item/"))
		for link in links:
			new_url = link['href']
			new_full_url = urljoin(page_url,new_url)
			# print(new_full_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self,page_url,soup):
		res_data = {}

		#<dd class="lemmaWgt-lemmaTitle-title"> <h1>PHP</h1>
		res_data['url'] = page_url

		title_node=soup.find('dd','lemmaWgt-lemmaTitle-title').find("h1")
		print(hasattr(title_node,'get_text'))
		if hasattr(title_node,'get_text') :
			res_data['title'] = title_node.get_text()
		else :
			res_data['title'] = '就没内容啊'

		#<div class="lemma-summary" label-module="lemmaSummary">	
		summary_node = soup.find('div',"lemma-summary")

		if hasattr(summary_node,'get_text') :

			res_data['summary'] = summary_node.get_text()
		else :
			res_data['summary'] = '就没内容啊'

		return res_data

	def parse(self,page_url,html_cout):
		if page_url is None or html_cout is None:
			return

		soup = BeautifulSoup(html_cout,'html.parser',from_encoding = 'utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data =self._get_new_data(page_url,soup)
		return new_urls,new_data
		