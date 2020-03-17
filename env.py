# import
import os

# var
instances_list = os.listdir('./config/instances')
cache_dir = './cache'
config_dir = './config'
instances_dir = './config/instances'

# 检查文件夹
if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)
if not os.path.exists(config_dir):
    os.mkdir(config_dir)
if not os.path.exists(instances_dir):
    os.mkdir(instances_dir)

default = input("是否使用已有实例[Y/N]：")
if default == "y" or default == "Y":
    print(instances_list)
    instances_choose = input("请选择实例名称：")
elif default == "n" or default == "N":
    instance_name = input("实例名称：")
    instance_path = input("实例（.minecraft）绝对路径：")
    instance_version = input("实例版本：")
    write_config = open('./config/instances/'+instance_name, 'a+')
    print("[PATH]", file=write_config)
    print(instance_path, file=write_config)
    print(instance_version, file=write_config)
    print("\033[1;33m 写入成功！\033[0m")
    write_config.close()
    instances_choose = instance_name
else:
    print("\033[1;31m 请重新检查输入!\033[0m")
