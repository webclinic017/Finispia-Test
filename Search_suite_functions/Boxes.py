from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from Selenium_Driver import getElementList,iselementClick,isElementPresent,getLocator,getLocatorType


def boxesVerification(box,question,popover):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    boxlocator=getLocator(box)
    boxlocatorType=getLocatorType(box)
    questionlocator=getLocator(question)
    questionlocatorType=getLocatorType(question)
    popoverlocator=getLocator(popover)
    popoverlocatorType=getLocatorType(popover)
    boxes_liste=getElementList(driver,boxlocator,boxlocatorType) 
    question_marks=getElementList(driver,questionlocator,questionlocatorType)      
    l=len(boxes_liste)
    if l!=6:
         BuiltIn().log("Boxes List contains uncertain number of elements==>"+str(l),level="error")
         assert False==True
    else:
        count=0
        j=0
        result=True
        for i in range(l-1):
            if (boxes_liste[i].text!="Fail") &  (boxes_liste[i].text!="Pass") & (boxes_liste[i].text!="Missing Data" ):
                BuiltIn().log("Text in box number "+str(i+1)+"is not accurate",level="error") 
                result= False
            elif boxes_liste[i].text=="Pass":
                count+=1
            elif boxes_liste[i].text=="Fail":
                if iselementClick(driver,element= question_marks[j]):
                    j+=1
                    if isElementPresent(driver,popoverlocator,popoverlocatorType)==False:
                         BuiltIn().log("Pop over in box number "+str(j+1)+"doesn't exist",level="error")
                         result= False
                else:
                     BuiltIn().log("Unable to click question mark number "+str(j+1),level="error")
                     result= False
    compliance_text=str(count)+"/5"
    if (boxes_liste[l-1].text == compliance_text) == False:
         BuiltIn().log("Compliance text is not acccurate",level="error")
         result= False
    if result:
        BuiltIn().log("Boxes verification is successful")
    else:
        BuiltIn().log("Boxes verification is unsuccessful",level="error")
        assert False==True


    





