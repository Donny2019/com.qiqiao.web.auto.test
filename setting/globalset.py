import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class UiPath:

    chrome_driver_path = base_path + "\\drivers\\chromedriver.exe"
    exe_path = base_path + "data\\exe\\upload.exe"
    file_path = base_path + "\\data\\file"
    xml_path = base_path + "\\elements"
    report_path = base_path + "\\reports"
    screenshot_path = base_path + "\\screenshots"
    cases_path = base_path + "\\cases"
    yaml_path = base_path + "\\config"