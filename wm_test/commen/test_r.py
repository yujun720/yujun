# coding:utf-8
import yaml,os,json
def read_yaml(source):
        # 获取当前脚本所在文件夹上一级目录
        curPath = os.path.dirname(os.path.dirname(__file__)) + "/source"
        print(curPath)
        # 获取yaml文件路径
        yamlPath = os.path.join(curPath, source)
        print(yamlPath)

        # open方法打开直接读出来
        f = open(yamlPath, 'r', encoding='utf-8')
        cfg = f.read()

        # print(type(cfg))  # 读出来是字符串
        # print(cfg)

        data = yaml.load(cfg,Loader=yaml.FullLoader)  # 用load方法转字典
        josn_data = json.dumps(data)    #转json格式
        return josn_data