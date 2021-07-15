from xml.dom.minidom import parse

from setting.globalset import UiPath
import yaml
import os


def readYaml(file_name, key=None, key1=None):
    '''读取yaml配置文件'''
    yamlPath = UiPath.yaml_path + "/" + file_name
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.safe_load(cfg)
    if key1 is None and key is None:
        f.close()
        return d
    elif key != None and key1 == None:
        f.close()
        return d[key]
    else:
        f.close()
        return d[key][key1]

def readXml(components, child_name):
    '''读取xml文件'''

    files = os.listdir(UiPath.xml_path)
    path = UiPath.xml_path
    for file in files:
        domtree = parse(os.path.join(path, file))
        rootnode = domtree.documentElement
        elements = rootnode.getElementsByTagName(components)
        try:
            loc = elements[0].getElementsByTagName(child_name)[0].getAttribute("loc")
        except:
            continue
        return loc