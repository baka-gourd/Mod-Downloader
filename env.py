# import
import os
import configparser

cfg = configparser.ConfigParser()
instances_config = 'instances.ini'
cache_dir = './cache'
cfg.read(instances_config)


# 检查文件
if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)
if not os.path.exists('./downloader.ini'):
    init_downloader = open("./downloader.ini", "a+")
    print("[downloader]", file=init_downloader)
    print("thread = 32", file=init_downloader)
    print("export = flase", file=init_downloader)
    init_downloader.close()

default = input("是否使用已有实例[Y/N]：")
if default == "y" or default == "Y":  # 选择配置
    instances_list = cfg.sections()
    for i in instances_list:
        print(i)
    instances_choose = input("请选择实例：")
elif default == "n" or default == "N":  # 写入配置
    instance_name = input("实例名称（不可相同！）：")
    instance_path = input("实例（.minecraft）绝对路径：")
    instance_version = input("实例版本：")
    cfg.add_section(instance_name)
    cfg.set(instance_name, "path", instance_path)
    cfg.set(instance_name, "version", instance_version)
    with open("./instances.ini", "w+") as icfg:
        cfg.write(icfg)
    instances_choose = instance_name
else:
    print("\033[1;31m 请重新检查输入!\033[0m")

using_path = cfg.get(instances_choose, "path")
using_version = cfg.get(instances_choose, "version")
