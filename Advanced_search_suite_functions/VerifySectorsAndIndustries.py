from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getElementList,iselementClick,getChildren,elementClick

def clickSectorInputField(driver,liste):
    number_tries=0
    while(number_tries<=5):
            number_tries+=1
            if iselementClick(driver,element=liste[0]):
                    sectors_list=getChildren(driver,"select2-results__options","li",parentlocatorType="class")
                    if len(sectors_list)>0:
                        break
                    else:
                            continue
            else:
                    continue
    return sectors_list
def selectSector(driver,sectors_list,sector_index):
        sector_name=sectors_list[sector_index].text
        number_tries_sectors=0
        sector_clicked=False
        while(number_tries_sectors<3):
                number_tries_sectors+=1
                if iselementClick(driver,element=sectors_list[sector_index]):
                        sector_clicked=True
                        break
                else:
                        continue
        if sector_clicked:
                BuiltIn().log("Sector "+sector_name+" is clicked successfully")
        else:
                BuiltIn().log("Unable to click sector "+sector_name)
        return sector_clicked

def verifyIndestries(driver,liste):
        number_tries_indestries=0
        indestries_found=False
        while(number_tries_indestries<5):
                number_tries_indestries+=1
                if iselementClick(driver,element=liste[1]):
                        BuiltIn().log("element is clicked")
                        indestries_list=getChildren(driver,"select2-results__options","li",parentlocatorType="class")
                        if len(indestries_list)>0:
                                BuiltIn().log(str(len(indestries_list))+" indestries found in this sector")
                                indestries_found=True
                                break
                        else:
                                continue
                else:
                        BuiltIn().log("Unable to clcik element")
                        continue
        if indestries_found==False:
                BuiltIn().log("No indestries found in this sector", level="error")
        return indestries_found

def verifySectorsAndIndustries():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    close_buttons=getElementList(driver,locator="close",locatorType="class")
    liste=getElementList(driver,locator="select2-search__field",locatorType="class")
    sectors_list=clickSectorInputField(driver,liste)
    if len(sectors_list)==0:
        BuiltIn().log("Unable to extract sectors",level="error")
        assert True==False
    else:
        result=True
        l=len(sectors_list)
        for i in range(l):
                if selectSector(driver,sectors_list,i):
                        liste=getElementList(driver,locator="select2-search__field",locatorType="class")
                        if verifyIndestries(driver,liste)==False:
                                result=False
                        elementClick(driver,element=close_buttons[2])
                        sectors_list=clickSectorInputField(driver,liste)
                else:
                        result=False
   
    assert result==True    
         


    

   