# python-spider
html_parser.py 里面的正则是根据页面的规则写的
此次爬去的是跟python词条有关的1000个词条
入口地址是：https://baike.baidu.com/item/Python/407313.htm
经检测得知，目前百度百科的词条规则是/item/xxxxx
所以，文件的正则也是这么写的
但是，后面百科的规则可能会变，如果有变动，那就需要更改我们的正则去匹配页面的a标签
