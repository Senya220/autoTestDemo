import os
import configparser
import handlePath

path = handlePath.get_Path()  # 调用实例化
config_path = os.path.join(path, 'config.ini')  # 在path路径下再加一级，即绝对路径\config.ini
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法，实例化config
config.read(config_path, encoding='utf-8')

#主要用来处理测试环境变量的读取
class ReadConfig():
     def get_http(self, name):
         value = config.get('HTTP', name)
         return value

     def get_email(self, name):
         value = config.get('EMAIL', name)
         return value

     def get_mysql(self, name):
         value = config.get('DATABASE', name)
         return value
