from selenium.webdriver import Chrome
from Base_Files import Intitiate_driver
from Library import Config_Reader
from Pages import Registration_Page
import pytest
#import openpyxl



@pytest.mark.parametrize('data',dataGenerator())
def test_validateregistration(data):
    driver = Intitiate_driver.Start_Browser()
    register = Registration_Page.Registration_done(driver)
    register.enter_username(data[0])
    register.enter_email("Bharatkannang@gmail.com")
    register.enter_password(data[1])
    register.enter_cpassword("Letmein@123")






    #driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration","username")).send_keys("Bharath")
    #driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration","email_name")).send_keys("bharatkannanG@gmail.com")
    #driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration","password_name").send_keys("Letmein@123")
    #driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration","cpassword_name").send_keys("Letmein@123")




