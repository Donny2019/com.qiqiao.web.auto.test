from basepage.base_driver import UiDriver
from tools.custom_method import readXml
from selenium import webdriver

class Login(UiDriver):
    def loginRuntimeBycookie(self,url):
        cookie = {'domain': '.qy.do1.com.cn',
                  'httpOnly': True,
                  'name': 'x-auth0-token',
                  'path': '/qiqiao2/runtime',
                  'secure': False,
                  'value': '39fc41a176a641042eb13cf6666c3c36'
                  }
        self.driver.get("https://qy.do1.com.cn/qiqiao2/runtime")
        self.driver.add_cookie(cookie)
        self.driver.get(url)


class Home(UiDriver):
    '''
    首页业务封装
    '''
    def clickWorkbenchButton(self):
        '''
        点击工作台按钮
        :return:
        '''
        loc = readXml("home","workbench")
        self.clickElement(loc)

    def clickAppListButton(self):
        '''
        点击应用列表按钮
        :return:
        '''
        loc = readXml("home","applist")
        self.clickElement(loc)

    def clickPendingListButton(self):
        '''
        点击待办列表
        :return:
        '''
        loc = readXml("home","pendnglist")
        self.clickElement(loc)


    def clickMoreButton(self):
        '''
        点击-更过按钮
        :return:
        '''
        loc = readXml("home","more")
        self.clickElement(loc)


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="D:\Program Files\com.qiqiao.web.auto.test\drivers\chromedriver.exe")
    Login(driver).loginRuntimeBycookie("https://qy.do1.com.cn/qiqiao2/runtime")
    Home(driver).clickWorkbenchButton()
    Home(driver).clickAppListButton()