# coding=utf-8
# import
import env
import linecache
import json
from env import instances_choose
from urllib.request import Request
from urllib.request import urlopen
from downloader import Downloader
from downloader import run

# var
downloader_config = "./config/downloader.ini"

# code

# 选择实例
#print("\033[1;32m 您选择的实例名称是：\033[0m" + instances_choose)
using_path = linecache.getline('./config/instances/' + instances_choose, 2)
using_version = linecache.getline('./config/instances/' + instances_choose, 3)
using_path = using_path[:-1]
using_version = using_version[:-1]
# print(using_path)
# print(using_version)

# 搜索
search_key = str("craft")  # input("请输入搜索关键词：")
page_count = str(1)

request = Request('https://addons-ecs.forgesvc.net/api/v2/addon/search?categoryId=0&gameId=432&gameVersion=' +
                  using_version+'&index='+page_count+'&pageSize=10&searchFilter='+search_key)

response_body_bytes = urlopen(request).read()
response_body_str = str(response_body_bytes, 'utf-8')
search_cache = open('./cache/search_cache.json', 'w')
print(response_body_str, file=search_cache)
search_cache_json = json.loads(response_body_str)
search_cache.close()
# 解析Json
for i in search_cache_json:
    project_name = i['name']  # 获取Mod名
    project_authors = i['authors']
    project_download = i['gameVersionLatestFiles']
    for version in project_download:
        if version['gameVersion'] == using_version:  # 获取ModID
            project_download_id = version['projectFileId']
            break
        else:
            pass
    for name in project_authors:  # 获取Mod作者
        project_authors_name = name['name']
        break
    print("ID:", project_download_id, "\t", project_name, "\t",
          project_authors_name, "\t")

print("fuck")
