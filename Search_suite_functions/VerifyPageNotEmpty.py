from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from Selenium_Driver import getChildren

def verifyPageNotEmpty():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    childrenlist=getChildren(driver,parentlocator="app-company-detail",childrenlocator="div",parentlocatorType="tag",childrenlocatorType="tag")
    if len(childrenlist) == 0 :
        BuiltIn().log("Page is empty",level="error")
        return True
    else:
        return False

