from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import Config_Reader

def Start_Browser():
    global driver
    if (Config_Reader.readConfigdata('Details','Browser') == 'chrome') :
        path = "/Users/bharathgnanasekar/Movies/Selenium/chromedriver 6"
        driver = Chrome(executable_path=path)
#Use Firefox browser

    elif (Config_Reader.readConfigdata('Details','Browser') == 'firefox'):
        path = "/Users/bharathgnanasekar/Movies/Selenium/geckodriver"
        driver = Firefox(executable_path=path)

    else :
        path = "/Users/bharathgnanasekar/Movies/Selenium/chromedriver 6"
        driver = Chrome(executable_path=path)


    driver.get(Config_Reader.readConfigdata('Details','Application_URL'))
    driver.maximize_window()
    return driver

def Close_Browser():

    driver.close()