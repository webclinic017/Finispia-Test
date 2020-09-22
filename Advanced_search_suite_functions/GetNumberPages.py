from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getChildren

def getNumberPages():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    pagination_elements=getChildren(driver,parentlocator="result-details",parentlocatorType="id",childrenlocator="li",childrenlocatorType="tag")
    if len(pagination_elements)==0 :
        BuiltIn().log("Unable to extract pagination elements",level="error")
        assert False==True
    pagination_elements.pop(0)
    pagination_elements.pop(-1)
    pagination_numbers=[]
    for p in pagination_elements :
        if str(p.text).isdigit() :
            pagination_numbers.append(p.text)
    useful_pagination_numbers=[]
    if len(pagination_numbers)>=3:
        useful_pagination_numbers.append(pagination_numbers[(len(pagination_numbers)-1)//2])
        useful_pagination_numbers.append(pagination_numbers[-1])
    elif len(pagination_numbers)==2:
        useful_pagination_numbers.append(pagination_numbers[-1])
    elif len(pagination_numbers)==0:
        BuiltIn().log("No digital numbers found in the bottom pagination  ====> Page is empty",level="error")
        assert False==True
    return useful_pagination_numbers
        
    

