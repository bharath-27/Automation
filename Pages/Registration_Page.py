from Library import Config_Reader

class Registration_done :

    def __init__(self,obj):
        global driver
        driver = obj

    def enter_username(self,username):
        driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration", "username")).send_keys(username)

    def enter_email(self,email):
        driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration", "email_name")).send_keys(email)

    def enter_password(self,password):
        driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration", "password_name").send_keys(password)

    def enter_cpassword(self,cpassword):
            driver.find_element_by_name(Config_Reader.fetchelementlocatos("Registration", "cpassword_name").send_keys(cpassword)

