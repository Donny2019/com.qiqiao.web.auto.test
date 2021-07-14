import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from retrying import retry

class UiDriver(object):

    def __init__(self,driver):
        '''
        运行初始化
        '''
        self.driver=driver

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def waitElement(self, by, value, secs=2):
        """
        等待元素显示
        """
        try:
            if by == "id":
                element = WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.ID, value)))
                self.driver.execute_script("arguments[0].scrollIntoView()",element)
            elif by == "name":
                element=WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.NAME, value)))
                self.driver.execute_script("arguments[0].scrollIntoView()", element)
            elif by == "class":
                element=WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                self.driver.execute_script("arguments[0].scrollIntoView()", element)
            elif by == "link_text":
                element=WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
                self.driver.execute_script("arguments[0].scrollIntoView()", element)
            elif by == "xpath":
                element=WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.XPATH, value)))
                self.driver.execute_script("arguments[0].scrollIntoView()", element)
            elif by == "css":
                element=WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
                self.driver.execute_script("arguments[0].scrollIntoView()", element)
            else:
                raise NoSuchElementException("找不到元素，请检查语法或元素")
        except TimeoutException:
            print("查找元素超时请检查元素")

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def getElement(self, css):
        """
        判断元素定位方式，并返回元素
        """
        if "=>" not in css:
            by = "css"
            value = css
            self.waitElement(by, css)
        else:
            by = css.split("=>")[0]
            value = css.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "语法错误，参考: 'id=>kw 或 xpath=>//*[@id='kw'].")
            self.waitElement(by, value)
        if by == "id":
            element = self.driver.find_element(By.ID,value)
        elif by == "name":
            element = self.driver.find_element(By.NAME,value)
        elif by == "class":
            element = self.driver.find_element(By.CLASS_NAME,value)
        elif by == "link_text":
            element = self.driver.find_element(By.LINK_TEXT,value)
        elif by == "xpath":
            element = self.driver.find_element(By.XPATH,value)
        elif by == "css":
            element = self.driver.find_element(By.CSS_SELECTOR,value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def getElements(self, css):
        """
        判断元素定位方式，并返回元素列表
        """

        if "=>" not in css:
            by = "css"
            value = css
            self.waitElement(by, css)
        else:
            by = css.split("=>")[0]
            value = css.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "语法错误，参考: 'id=>kw 或 xpath=>//*[@id='kw'].")
            self.waitElement(by, value)
        if by == "id":
            elements = self.driver.find_elements(By.ID,value)
        elif by == "name":
            elements = self.driver.find_elements(By.NAME,value)
        elif by == "class":
            elements = self.driver.find_elements(By.CLASS_NAME,value)
        elif by == "link_text":
            elements = self.driver.find_elements(By.LINK_TEXT,value)
        elif by == "xpath":
            elements = self.driver.find_elements(By.XPATH,value)
        elif by == "css":
            elements = self.driver.find_elements(By.CSS_SELECTOR,value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return elements


    def openUrl(self, url):
        """
        打开url.并窗口最大化
        用法:
        driver.open("https://www.baidu.com")
        """
        self.driver.get(url)
        self.driver.maximize_window()


    def setWindowSize(self, wide, high):
        """
        设置浏览器窗口宽和高.
        用法:
        driver.set_window(wide,high)
        """
        self.driver.set_window_size(wide, high)

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def sendKeys(self, css, text):
        """
        操作输入框.
        用法:
        driver.type("css=>#el","selenium")
        """
        el = self.getElement(css)
        el.send_keys(text)

    def clear(self, css):
        """
        清除输入框的内容.
        用法:
        driver.clear("css=>#el")
        """
        el = self.getElement(css)
        el.clear()

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def clickElement(self, css):
        """
        它可以点击任何文本/图像
        连接，复选框，单选按钮，甚至下拉框等等..
        用法:
        driver.click("css=>#el")
        """
        el = self.getElement(css)
        el.click()

    def rightClick(self, css):
        """
        右键单击元素.
        用法:
        driver.right_click("css=>#el")
        """
        el = self.getElement(css)
        ActionChains(self.driver).context_click(el).perform()

    def moveToElement(self, css):
        """
        鼠标移到元素（悬停）.
        用法:
        driver.move_to_element("css=>#el")
        """
        el = self.getElement(css)
        self.driver.execute_script("arguments[0].scrollIntoView()",el)
        ActionChains(self.driver).move_to_element(el).perform()

    def doubleClick(self, css):
        """
        双击元素.
        用法:
        driver.double_click("css=>#el")
        """
        el = self.getElement(css)
        ActionChains(self.driver).double_click(el).perform()

    def dragAndDrop(self, el_css, ta_css):
        """
        把一个元素拖到一定的距离，然后把它放下.
        用法:
        driver.drag_and_drop("css=>#el","css=>#ta")
        """
        element = self.getElement(el_css)
        target = self.getElement(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()


    def quit(self):
        """
        关闭使用的所有窗口.
        用法:
        driver.quit()
        """
        self.driver.quit()


    def F5(self):
        """
        刷新当前页面.
        用法:
        driver.F5()
        """
        time.sleep(1)
        self.driver.refresh()

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def js(self, script,element):
        """
        执行JavaScript脚本.
        用法:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script,element)

    def getAttribute(self, css, attribute):
        """
        获取元素属性的值.
        用法:
        driver.get_attribute("css=>#el","type")
        """
        el = self.getElement(css)
        return el.get_attribute(attribute)

    def addAttribute(self,css,attribute,value):
        '''
        添加元素的属性值
        用法：
        dricer.addAttribute("css=>#test","id","exmpname")
        '''
        el=self.getElement(css)
        try:
            self.driver.execute_script("arguments[0].%s=arguments[1]" % attribute, el, value)
        except Exception:
            raise


    def removeAttribute(self,css,attribute):
        '''
        删除元素属性值
        用法：
        driver.removeAttribute("css=>#test","id")
        '''
        element = self.getElement(css)
        try:
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1])", element, attribute)
        except Exception:
            raise

    def getText(self, css):
        """
        获得元素文本信息
        用法:
        driver.get_text("css=>#el")
        """
        el = self.getElement(css)
        return el.text


    def getTitle(self):
        """
        得到窗口标题.
        用法:
        driver.get_title()
        """
        return self.driver.title

    def getUrl(self):
        """
        获取当前页面的URL地址.
        用法:
        driver.get_url()
        """
        return self.driver.current_url

    def getAlertText(self):
        """
        得到警报的文本.
        用法:
        driver.get_alert_text()
        """
        return self.driver.switch_to.alert.text

    def wait(self, secs):
        """
        隐式等，页面上的所有元素.
        用法:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secs)

    def acceptAlert(self):
        """
        接受警告框.
        用法:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismissAlert(self):
        """
        Dismisses the alert available.
        用法:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def switchToFrame(self, css):
        """
        切换到指定的frame.
        用法:
        driver.switch_to_frame("css=>#el")
        """
        iframe_el = self.getElement(css)
        self.driver.switch_to.frame(iframe_el)

    def switchFrameOut(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, css):
        """
        打开新窗口并切换到新打开的窗口.
        用法:
        传入一个点击后会跳转的元素
        driver.open_new_window("link_text=>注册")
        """
        original_window = self.driver.current_window_handle
        el = self.getElement(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)

    def getScreenshot(self,file_path):
        """将当前窗口的屏幕截图保存到PNG图像文件中.
        用法:
        driver.get_screen_shot('/Screenshots/foo.png')
        """
        # self.driver.get_screenshot_as_base64()
        self.driver.save_screenshot(file_path)


    def addCookie(self,cookie):
        self.driver.add_cookie(cookie)