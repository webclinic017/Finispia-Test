from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getLocator,getLocatorType,iselementClick

def clickAddToPortfolioBtn(locator):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    btn_locator=getLocator(locator)
    btn_locatorType=getLocatorType(locator)
    number_tries=0
    clicked=False
    while(number_tries<5):
        number_tries+=1
        if iselementClick(driver,locator=btn_locator,locatorType=btn_locatorType):
            clicked=True
            break
    if clicked:
        BuiltIn().log("Add to portfolio btn is clicked successfully")
    else:
        BuiltIn().log("Unable to click Add to portfolio btn",level="error")
    assert clicked==True