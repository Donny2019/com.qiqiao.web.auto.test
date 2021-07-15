from basepage.base_driver import UiDriver
from tools.custom_method import readXml
from tools.custom_method import readYaml



class LoginRuntime(UiDriver):

    def byCookie(self):
        cookie = {'domain': '.qy.do1.com.cn',
                  'httpOnly': True,
                  'name': 'x-auth0-token',
                  'path': '/qiqiao2/runtime',
                  'secure': False,
                  'value': '39fc41a176a641042eb13cf6666c3c36'
                  }
        self.driver.get("https://qy.do1.com.cn/qiqiao2/runtime")
        self.driver.add_cookie(cookie)
        self.driver.get("https://qy.do1.com.cn/qiqiao2/runtime")