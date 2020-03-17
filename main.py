# coding=utf-8
# import
import linecache
import json
import configparser
import os
from urllib.request import Request
from urllib.request import urlopen

from env import using_path
from env import using_version
from downloader import Downloader


cfg = configparser.ConfigParser()
downloader_config = './downloader.ini'

cfg.read(downloader_config)
cfg_downloader_thread = cfg.getint("downloader", "thread")

# 搜索
search_key = str(input("请输入搜索关键（输入exit结束搜索）："))
page_count = str(1)
if search_key == "exit":
    print("结束搜索，开始下载...")
else:
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


mod_download = Downloader(
    'https://i.mcmod.cn/class/cover/20200201/1580541817_7366_sJyD.jpg', cfg_downloader_thread, "rua.jpg")
mod_download.drun()
