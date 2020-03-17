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
search_key = ""
mod_id_download_list = []
mod_file_id_download_list = []
mod_name_download_list = []

cfg.read(downloader_config)
cfg_downloader_thread = cfg.getint("downloader", "thread")

# 搜索
while search_key != 'exit':
    search_key = str(input("请输入搜索关键词（输入exit结束搜索）："))
    page_count = str(1)
    if search_key == "exit":
        print("结束搜索，开始下载...")
    else:
        project_num = 0
        project_download_id_dict = {}
        project_id_dict = {}
        project_name_dict = {}
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
            project_id = i['id']
            project_authors = i['authors']
            project_download = i['gameVersionLatestFiles']
            for version in project_download:
                if version['gameVersion'] == using_version:  # 获取Mod文件ID
                    project_download_id = version['projectFileId']
                    break
                else:
                    pass
            for name in project_authors:  # 获取Mod作者
                project_authors_name = name['name']
                break
            print(project_num, "\t", project_name, "\t",
                  project_authors_name, "\t")
            project_download_id_dict[project_num] = project_download_id
            project_id_dict[project_num] = project_id
            project_name_dict[project_num] = project_name
            project_num = project_num + 1
        select_mod_num = int((input("请输入mod编号：")))
        mod_id_download_list.append(
            project_id_dict[select_mod_num])
        mod_file_id_download_list.append(
            project_download_id_dict[select_mod_num])
        mod_name_download_list.append(project_name_dict[select_mod_num])
else:
    pass


# print(project_download_id_dict)
# print(project_id_dict)
# print(project_name_dict)
# print(mod_id_download_list)
# print(mod_file_id_download_list)
# print(mod_name_download_list)

download_num = len(mod_id_download_list)
download_num_use = download_num - 1
# print(download_num)
while download_num_use >= 0:
    download_cache_id = str(mod_id_download_list[download_num_use])
    download_cache_file_id = str(mod_file_id_download_list[download_num_use])
    download_cache_file_name = str(mod_name_download_list[download_num_use])
    request = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + download_cache_id + '/file/' + download_cache_file_id + '/download-url')
    response_download_body_bytes = urlopen(request).read()
    response_download_body_str = str(response_download_body_bytes, 'utf-8')
    #print(response_download_body_str)
    mod_download = Downloader(
        response_download_body_str, cfg_downloader_thread, using_path + "\\mods\\" + download_cache_file_name + ".jar")
    mod_download.drun()
    download_num_use = download_num_use - 1
else:
    pass
