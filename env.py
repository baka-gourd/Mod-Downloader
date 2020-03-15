# import
import os

# class


class FontColor(object):
    GREEN = '\033[32m'
    RED = '\033[31m'
    YELLOW = '\33[33m'


# var
fc = FontColor()
instances_list = os.listdir('./config/instances')

# code
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
    print(fc.GREEN+"写入成功！")
    write_config.close()
    instances_choose = instance_name
else:
    print(fc.RED+"请重新检查输入!")
