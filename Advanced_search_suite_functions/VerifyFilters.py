from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getChildren,getElementList,isElementDisplayed

def getNumberFilters():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    nb_filters=getChildren(driver,parentlocator="additional-filters",parentlocatorType="class",childrenlocator="tr",childrenlocatorType="tag")
    return len(nb_filters)

def verifyFilterIsSelected(index):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    liste=getElementList(driver,locator="finispia-input",locatorType="class")#The first element in this list is the price field the others are the filters input
    return isElementDisplayed(driver,element=liste[index])
