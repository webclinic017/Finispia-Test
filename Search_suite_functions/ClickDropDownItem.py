from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getChildren,elementClick

def isDropDownItemClicked():
        se2lib = BuiltIn().get_library_instance("Selenium2Library")
        driver = se2lib._current_browser()
        try:
                serach_results_elements=getChildren(driver,parentlocator="typeahead-container",childrenlocator="button",parentlocatorType="tag",childrenlocatorType="tag")
                elementClick(driver,element=serach_results_elements[0])
                BuiltIn().log("Drop down item is clicked successfully")
                return True
        except:
                BuiltIn().log("can not click drop down item",level="error")
                return False
