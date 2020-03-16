# coding=utf-8
# import
import env
import linecache
import json
from env import instances_choose
from urllib.request import Request
from urllib.request import urlopen

# var
downloader_config = "./config/downloader.ini"

# code

# 选择实例
print("您选择的实例名称是：" + instances_choose)
using_path = linecache.getline('./config/instances/' + instances_choose, 2)
using_version = linecache.getline('./config/instances/' + instances_choose, 3)
using_path = using_path[:-1]
using_version = using_version[:-1]
print(using_path)
print(using_version)

# 搜索
search_key = str("craft")  # input("请输入搜索关键词：")
page_count = str(1)

request = Request('https://addons-ecs.forgesvc.net/api/v2/addon/search?categoryId=0&gameId=432&gameVersion=' +
                  using_version+'&index='+page_count+'&pageSize=10&searchFilter='+search_key)

response_body = urlopen(request).read()
search_cache = open('./cache/search_cache.json', 'w')
print(response_body, file=search_cache)
search_cache.close()

with open('./cache/search_cache.json', encoding='utf-8') as s_c:
    line = s_c.readline()
    d = json.loads(line)
    name = d['name']
    authors = d['company_url']
    s_c.close()
