from basepage.base_driver import UiDriver
from tools.custom_method import readXml

class Login(UiDriver):
    def loginRuntimeBycookie(self,url):
        cookie = {'domain': '.qy.do1.com.cn',
                  'httpOnly': True,
                  'name': 'x-auth0-token',
                  'path': '/qiqiao2/runtime',
                  'secure': False,
                  'value': '9019ff133344e1d33f8ad275a10f52f0'
                  }
        self.driver.get("https://qy.do1.com.cn/qiqiao2/runtime")
        self.driver.add_cookie(cookie)
        self.driver.get(url)


class Home(UiDriver):
    def clickWorkbenchButton(self):
        self.clickElement()