from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getLocator,getLocatorType,getElement

def Title(title,companyname):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    titlelocator=getLocator(title)
    titlelocatorType=getLocatorType(title)
    try:
        title_element= getElement(driver,titlelocator,titlelocatorType)
        if title_element.text==companyname:
            return True
        else:
            return False
    except:
        BuiltIn().log("Unable to locate the title")
        return True #This function returns false only if the title is not exact not when it doesn't exist 
        

