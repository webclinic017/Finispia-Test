from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getChildren,sendKeys,getElement
import random
import string

def changePassword(old_password,new_password):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    parent = getElement(driver,locator="//tab[@heading='Password']",locatorType="xpath")
    inputs_list=getChildren(driver,childrenlocator="input",childrenlocatorType="tag",parent=parent)
    data_is_sent=False
    if sendKeys(driver,element=inputs_list[0],data=old_password):
        if sendKeys(driver,element=inputs_list[1],data=new_password):
            if sendKeys(driver,element=inputs_list[2],data=new_password):
                data_is_sent=True
            else:
                BuiltIn().log("Unable to send data in the third firld",level="error")
        else:
            BuiltIn().log("Unable to send data in the second field",level="error")
    else:
        BuiltIn().log("Unable to send data in the first field",level="error")
    assert data_is_sent==True



