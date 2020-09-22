from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def getByType(locatorType):
    locatorType = locatorType.lower()
    if locatorType == "id":
        return By.ID
    elif locatorType == "name":
        return By.NAME
    elif locatorType == "xpath":
        return By.XPATH
    elif locatorType == "css":
        return By.CSS_SELECTOR
    elif locatorType == "class":
        return By.CLASS_NAME
    elif locatorType == "link":
        return By.LINK_TEXT
    elif locatorType =="tag":
        return By.TAG_NAME


def getElement(driver,locator, locatorType="id"):
    element = None
    locatorType = locatorType.lower()
    byType = getByType(locatorType)
    ignored_exceptions=(StaleElementReferenceException)
    try:
        element = WebDriverWait(driver,30,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((byType, locator)))
        #element = driver.find_element(byType, locator)  
        return element
    except:
        return element

def getChildren(driver,parentlocator="",childrenlocator="",parentlocatorType="id",childrenlocatorType="tag",parent=None):
    childrenlist= []
    if parentlocator:
        parent=getElement(driver,parentlocator,parentlocatorType)
    childrenlocatorType = childrenlocatorType.lower()
    byType=getByType(childrenlocatorType)
    try:
        childrenlist=parent.find_elements(byType,childrenlocator)
        return childrenlist
    except:
        return childrenlist

def getElementList(driver,locator, locatorType="id"):
    elementlist= None
    locatorType = locatorType.lower()
    byType = getByType(locatorType)
    elementlist = driver.find_elements(byType, locator)      
    return elementlist

def elementClick(driver, locator="", locatorType="id",element=None):
    if locator:
        locatorType = locatorType.lower()
        byType = getByType(locatorType)
        ignored_exceptions=(StaleElementReferenceException)
        element = WebDriverWait(driver,30,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((byType, locator)))
    element.click()

def iselementClick(driver, locator="", locatorType="id",element=None):
    if locator:
        locatorType = locatorType.lower()
        byType = getByType(locatorType)
        ignored_exceptions=(StaleElementReferenceException)
        element = WebDriverWait(driver,30,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((byType, locator)))
    try:
        element.click()
        return True
    except:
        return False
    
    

def isElementPresent(driver, locator="", locatorType="id", element=None):
    try:
        if locator:  # This means if locator is not empty
            element = getElement(driver,locator, locatorType)
        if element is not None:
            return True
        else:
            return False
    except:
        return False

def isElementDisplayed(driver,locator="",locatorType="id",element=None):
    if locator: # This means if the locator is not empty
        element = getElement(driver,locator,locatorType)
    if element.is_displayed():
        return True
    else:
        return False

        
def getLocator(scalar):
    return scalar[scalar.index("=")+1::]

def getLocatorType(scalar):
    return scalar[:scalar.index("=")]

def sendKeys(driver, locator="", locatorType="",element=None, data=""):
    try:
        if locator : #This means if locator is not empty
            element=getElement(driver,locator, locatorType)
        element.clear()
        element.send_keys(data)
        return True
    except:
        return False
        
        