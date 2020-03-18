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
select_mod_num = ""
select_mod_num_v = "1"
mod_id_download_list = []
mod_file_id_download_list = []
mod_name_download_list = []
dependencies_id_list = []
dependencies_id_list_2 = []
dependencies_id_list_3 = []
dependencies_id_list_4 = []
fuck_id_list = []
fuck_name_list = []
project_authors_name = ""
project_download_id = ""

cfg.read(downloader_config)
cfg_downloader_thread = cfg.getint("downloader", "thread")
cfg_downloader_export = cfg.get("downloader", "export")

# 搜索
while search_key != 'exit':
    search_key = str(input("请输入搜索关键词（输入exit结束搜索）："))
    search_key = search_key.replace('\u0020', '+')
    page_count = str(1)
    if search_key == "exit":
        print("结束搜索，开始解析依赖...")
    else:
        select_mod_num_v = "1"
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
        while str(select_mod_num) != "back" and select_mod_num_v != "0":
            select_mod_num = (input("请输入mod编号（若无mod，使用back重新搜索）："))
            try:
                select_mod_num_t = int(select_mod_num)
            except ValueError:
                select_mod_num_v = "1"
            else:
                select_mod_num_v = "0"
        else:
            if select_mod_num == "back":
                select_mod_num = ""
            else:
                for num_ in select_mod_num:
                    select_mod_num_1 = int(num_)
                    mod_id_download_list.append(
                        project_id_dict[select_mod_num_1])
                    mod_file_id_download_list.append(
                        project_download_id_dict[select_mod_num_1])
                    mod_name_download_list.append(
                        project_name_dict[select_mod_num_1])

else:
    pass


# print(project_download_id_dict)
# print(project_id_dict)
# print(project_name_dict)
# print(mod_id_download_list)
# print(mod_file_id_download_list)
# print(mod_name_download_list)


for mod_id in mod_id_download_list:
    mod_id_str = str(mod_id)
    request_dependencies = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + mod_id_str + "/files")
    response_dependencies_body = urlopen(request_dependencies).read()
    response_dependencies_body_str = str(response_dependencies_body, 'utf-8')
    dependencies_cache = open('./cache/dependencies_cache.json', 'w')
    print(response_dependencies_body_str, file=dependencies_cache)
    dependencies_json = json.loads(response_dependencies_body_str)
    dependencies_cache.close()
    # 解析依赖Json
    for i in dependencies_json:
        dependencies_addonid = ""
        dependencies_gameVersion = i['gameVersion']
        dependencies = i['dependencies']
        if dependencies_gameVersion == [using_version]:
            for j in dependencies:
                addid_1 = str(j)
                addid = addid_1[12:-12]
                if addid not in dependencies_id_list:
                    dependencies_id_list.append(addid)
                else:
                    pass

        else:
            pass

for mod_id in dependencies_id_list:
    mod_id_str = str(mod_id)
    request_dependencies_2 = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + mod_id_str + "/files")
    response_dependencies_body_2 = urlopen(request_dependencies_2).read()
    response_dependencies_body_str_2 = str(
        response_dependencies_body_2, 'utf-8')
    dependencies_cache_2 = open('./cache/dependencies_cache_2.json', 'w')
    print(response_dependencies_body_str_2, file=dependencies_cache_2)
    dependencies_json_2 = json.loads(response_dependencies_body_str_2)
    dependencies_cache_2.close()
    # 解析依赖Json
    for i in dependencies_json_2:
        dependencies_addonid = ""
        dependencies_gameVersion = i['gameVersion']
        dependencies = i['dependencies']
        if dependencies_gameVersion == [using_version]:
            for j in dependencies:
                addid_1 = str(j)
                addid = addid_1[12:-12]
                if addid not in dependencies_id_list:
                    dependencies_id_list_2.append(addid)
                else:
                    pass

        else:
            pass

for mod_id in dependencies_id_list_2:
    mod_id_str = str(mod_id)
    request_dependencies_3 = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + mod_id_str + "/files")
    response_dependencies_body_3 = urlopen(request_dependencies_3).read()
    response_dependencies_body_str_3 = str(
        response_dependencies_body_3, 'utf-8')
    dependencies_cache_3 = open('./cache/dependencies_cache_3.json', 'w')
    print(response_dependencies_body_str_3, file=dependencies_cache_3)
    dependencies_json_3 = json.loads(response_dependencies_body_str_3)
    dependencies_cache_3.close()
    # 解析依赖Json
    for i in dependencies_json_3:
        dependencies_addonid = ""
        dependencies_gameVersion = i['gameVersion']
        dependencies = i['dependencies']
        if dependencies_gameVersion == [using_version]:
            for j in dependencies:
                addid_1 = str(j)
                addid = addid_1[12:-12]
                if addid not in dependencies_id_list_2:
                    dependencies_id_list_3.append(addid)
                else:
                    pass

        else:
            pass

for mod_id in dependencies_id_list_3:
    mod_id_str = str(mod_id)
    request_dependencies_4 = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + mod_id_str + "/files")
    response_dependencies_body_4 = urlopen(request_dependencies_4).read()
    response_dependencies_body_str_4 = str(
        response_dependencies_body_4, 'utf-8')
    dependencies_cache_4 = open('./cache/dependencies_cache_4.json', 'w')
    print(response_dependencies_body_str_4, file=dependencies_cache_4)
    dependencies_json_4 = json.loads(response_dependencies_body_str_4)
    dependencies_cache_4.close()
    # 解析依赖Json
    for i in dependencies_json_4:
        dependencies_addonid = ""
        dependencies_gameVersion = i['gameVersion']
        dependencies = i['dependencies']
        if dependencies_gameVersion == [using_version]:
            for j in dependencies:
                addid_1 = str(j)
                addid = addid_1[12:-12]
                if addid not in dependencies_id_list_3:
                    dependencies_id_list_4.append(addid)
                else:
                    pass

        else:
            pass

for i in dependencies_id_list:
    if i not in dependencies_id_list_2:
        dependencies_id_list_2.append(i)
    else:
        pass
for j in dependencies_id_list_2:
    if j not in dependencies_id_list_3:
        dependencies_id_list_3.append(j)
    else:
        pass
for k in dependencies_id_list_3:
    if k not in dependencies_id_list_4:
        dependencies_id_list_4.append(k)
    else:
        pass

# print(dependencies_id_list_4)


for dependencies_fuck_id in dependencies_id_list_4:
    fuck_str = str(dependencies_fuck_id)
    request_fuck_cf = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + fuck_str + "/files")
    response_fuck_cf_body = urlopen(request_fuck_cf).read()
    response_fuck_cf_body_str = str(
        response_fuck_cf_body, 'utf-8')
    dependencies_cache_fuck = open('./cache/dependencies_cache_fuck.json', 'w')
    print(response_fuck_cf_body_str, file=dependencies_cache_fuck)
    dependencies_cache_fuck_json = json.loads(
        response_fuck_cf_body_str)
    dependencies_cache_fuck.close()
    # 解析依赖Json
    for i in dependencies_cache_fuck_json:
        fuck_gameVersion = i['gameVersion']
        if fuck_gameVersion == [using_version]:
            fuck_id = i['id']
            fuck_name = i['fileName']
            fuck_id_list.append(int(fuck_id))
            fuck_name_list.append(fuck_name)
            break
        else:
            pass

# print(dependencies_id_list_4)
# print(fuck_id_list)
# print(fuck_name_list)

fuck_num = len(fuck_id_list)
fuck_num_use = fuck_num - 1

while fuck_num_use >= 0:
    fuck_mod_id = str(dependencies_id_list_4[fuck_num_use])
    fuck_id = str(fuck_id_list[fuck_num_use])
    fuck_name = str(fuck_name_list[fuck_num_use])
    request_fuck = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + fuck_mod_id + '/file/' + fuck_id + '/download-url')
    response_fuck_body_bytes = urlopen(request_fuck).read()
    response_fuck_body_str = str(response_fuck_body_bytes, 'utf-8')
    if cfg_downloader_export == 'true':
        export_cache = open('./url.txt', 'a+')
        print(response_fuck_body_str, file=export_cache)
        export_cache.close()
    else:
        pass
    fuck_download = Downloader(
        response_fuck_body_str, cfg_downloader_thread, using_path + "\\mods\\" + fuck_name + ".jar")
    fuck_download.drun()
    fuck_num_use = fuck_num_use - 1
else:
    pass


download_num = len(mod_id_download_list)
download_num_use = download_num - 1
# print(download_num)
while download_num_use >= 0:
    download_cache_id = str(mod_id_download_list[download_num_use])
    download_cache_file_id = str(mod_file_id_download_list[download_num_use])
    download_cache_file_name = str(mod_name_download_list[download_num_use])
    request_d = Request(
        'https://addons-ecs.forgesvc.net/api/v2/addon/' + download_cache_id + '/file/' + download_cache_file_id + '/download-url')
    response_download_body_bytes = urlopen(request_d).read()
    response_download_body_str = str(response_download_body_bytes, 'utf-8')
    if cfg_downloader_export == 'true':
        export_cache = open('./url.txt', 'a+')
        print(response_download_body_str, file=export_cache)
        export_cache.close()
    else:
        pass
    mod_download = Downloader(
        response_download_body_str, cfg_downloader_thread, using_path + "\\mods\\" + download_cache_file_name + ".jar")
    mod_download.drun()
    download_num_use = download_num_use - 1
else:
    pass
