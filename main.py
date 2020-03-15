# import
import env
import linecache
from env import instances_choose

# var
downloader_config = "./config/downloader.ini"
# code
print("您选择的实例名称是：" + instances_choose)
using_path = linecache.getline('./config/instances/' + instances_choose, 2)
using_version = linecache.getline('./config/instances/' + instances_choose, 3)
using_path = using_path[:-1]
using_version = using_version[:-1]
print(using_path)
print(using_version)
