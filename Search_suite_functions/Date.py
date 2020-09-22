from datetime import date,datetime
from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from Selenium_Driver import getElement,getLocator,getLocatorType

def verifyCloseDate(date_element):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    try :
        date_element_locator=getLocator(date_element)
        date_element_locatorType=getLocatorType(date_element)
        at_close_date_item_text=getElement(driver,locator=date_element_locator,locatorType=date_element_locatorType).text
        at_close_date_item=at_close_date_item_text[28::]
        BuiltIn().log("At close date "+at_close_date_item)
        at_close_date=datetime.strptime(at_close_date_item, "%Y/%m/%d")
        today_date=datetime.strptime(date.today().strftime("%Y/%m/%d"),"%Y/%m/%d")
        days_difference = (today_date - at_close_date).days
        if days_difference<=7:
            BuiltIn().log("Date is accurate ==> Less than a week")
        else:
            BuiltIn().log("Date is not accurate ==> More than a week",level="error")
            assert False==True
    except:
        BuiltIn().log("Unable to extract date",level="error")
        assert False==True
        
        
    
        

    
       
