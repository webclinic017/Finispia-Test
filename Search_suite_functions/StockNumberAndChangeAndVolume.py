from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from Selenium_Driver import getLocator,getLocatorType,getElementList 


def stockNumberAndchangeAndvolumeVerification(stock_change_volume):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    names=["Stock Number","change","volume"]
    locator= getLocator(stock_change_volume)
    locatorType= getLocatorType(stock_change_volume)
    liste=getElementList(driver,locator, locatorType)
    if len(liste)==0:
        BuiltIn().log("Stock Number and Volume and change elments do not exist",level="error")
        assert False==True
  
    elif len(liste)!=3:
        BuiltIn().log("Uncertain number of elements found ==>"+str(len(liste)),level="error")
        assert False==True
    else:
        result=True
        for i in range(3):
            if i!=0:
                if liste[i].text!="":
                    BuiltIn().log(names[i]+" Verification successful")
                else:
                    BuiltIn().log(names[i]+" Verification unsuccessful")
                    result=False
                    
            else:
                if liste[i].text!="$":
                    BuiltIn().log(names[i]+" Verification successful")
                else:
                    BuiltIn().log(names[i]+" Verification unsuccessful")
                    result=False
        if result:
            BuiltIn().log("Stock Number, change ad volume are accurate")
        else:
            BuiltIn().log("Stock Number, change ad volume are not accurate",level="error")
            assert True==False
    


