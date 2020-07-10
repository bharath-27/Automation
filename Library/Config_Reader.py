import configparser

def readConfigdata(section,key):
    cfg = configparser.ConfigParser()
    cfg.read("/Users/bharathgnanasekar/PycharmProjects/EndtoEndAutomation/Configuration_data/Config.cfg")
    return cfg.get(section,key)

def fetchelementlocatos(section,key):
    cfg = configparser.ConfigParser()
    cfg.read("/Users/bharathgnanasekar/PycharmProjects/EndtoEndAutomation/Configuration_data/Element_Locators.cfg")
    return cfg.get(section, key)

