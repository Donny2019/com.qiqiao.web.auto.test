import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class UiPath:

    chrome_driver_path = base_path + "\\ui\\drivers\\chromedriver.exe"
    exe_path = base_path + "\\ui\\data\\exe\\upload.exe"
    file_path = base_path + "\\ui\\data\\file"
    xml_path = base_path + "\\ui\\elements"
    report_path = base_path + "\\ui\\reports"
    screenshot_path = base_path + "\\ui\\screenshots"
    cases_path = base_path + "\\ui\\cases"
    yaml_path = base_path + "\\ui\\config"