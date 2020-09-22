from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import iselementClick,getChildren

def selectCountry(country_name):
        se2lib = BuiltIn().get_library_instance("Selenium2Library")
        driver = se2lib._current_browser()
        number_tries=0
        selected=False
        while(number_tries<=5):
                number_tries+=1
                if iselementClick(driver,locator="//span[@role='combobox']",locatorType="xpath"):
                        countries_list=getChildren(driver,"select2-results__options","li",parentlocatorType="class")
                        if len(countries_list)>1:
                                for i in range (len(countries_list)):
                                        if countries_list[i].text == country_name:
                                                index=i
                                                break
                                if iselementClick(driver,element=countries_list[index]):
                                        BuiltIn().log(country_name+" is selected successfully")
                                        selected=True
                                        break
                                else:
                                        continue
                        else:
                                continue
        
                else:
                        continue
        if selected==False:
                BuiltIn().log("Unable to select country "+country_name,level="error") 
        assert selected==True

                


    
