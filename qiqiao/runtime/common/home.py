from basepage.base_driver import UiDriver
from tools.custom_method import readXml
from tools.custom_method import readYaml
from selenium import webdriver




class Workbench(UiDriver):
    "工作台"
    def clickWorkbenchButton(self):
        '''
        点击工作台按钮
        :return:
        '''
        loc = readXml("home","workbench")
        self.clickElement(loc)

class APPList(UiDriver):
    "应用列表"
    def clickAppListButton(self):
        '''
        点击应用列表按钮
        :return:
        '''
        loc = readXml("home","applist")
        self.clickElement(loc)

class PendingList(UiDriver):
    "待办列表"
    def clickPendingListButton(self):
        '''
        点击待办列表
        :return:
        '''
        loc = readXml("home","pendnglist")
        self.clickElement(loc)
class More(UiDriver):
    "更多"
    def clickMoreButton(self):
        '''
        点击-更过按钮
        :return:
        '''
        loc = readXml("home","more")
        self.clickElement(loc)

class StartProcess(UiDriver):
    "发起流程"


class GlobalSearch(UiDriver):
    "全局搜索"


class HelpCenter(UiDriver):
    "帮助中心"


class MessageCenter(UiDriver):
    "消息中心"


class PersonalCenter(UiDriver):
    "个人中心"
