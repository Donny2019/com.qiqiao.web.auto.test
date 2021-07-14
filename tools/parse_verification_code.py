import os
import traceback
from PIL import Image
from io import BytesIO
import time
import pytesseract



def screenshot_code(driver, veri_code_xpath):
    """
    截图验证码图片
    :param veri_code_xpath: 验证码图片的xpath
    :return: 验证码图片
    """
    element_screen = driver.find_element_by_xpath(veri_code_xpath)
    location = element_screen.location
    size = element_screen.size
    # 截取当前窗口保存为png
    graph_ver_code = driver.get_screenshot_as_png()

    # 打开截图定位要截取的位置
    image = Image.open(BytesIO(graph_ver_code))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    image = image.crop((left, top, right, bottom))
    return image


def edit_picture(image):
    """
    图片二值化，增加识别率
    :param image:
    :return:
    """
    image = Image._conv_type_shape('L')
    rows, cols = image.size
    for i in range(rows):
        for j in range(cols):
            pixel = image.getpixel((i, j))
            if pixel > 150:
                image.putpixel((i, j), 255)
            elif pixel < 130:
                image.putpixel((i, j), 0)
    pic_name = time.strftime("%Y%m%d%H%M%S", time.localtime())
    current_path = os.getcwd()
    father_path = os.path.dirname(current_path)
    image_path = r'D:\Program Files\MyProjects\com.qiqiao.web.auto.test\data\%s.png' % pic_name
    image.save(image_path)
    return image_path


def recognize_captcha(image_path):
    """
    识别验证码
    :param image_path:
    :return:返回识别的验证码
    """
    image = Image.open(image_path)
    code = pytesseract.image_to_string(image)
    print(code)
