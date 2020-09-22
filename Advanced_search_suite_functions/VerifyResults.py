from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getChildren,getElement



def verifyResults(halal):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    table_titles=["Add to Portfolio","Symbol","Name","Exchange","Price","Pass/Fail"]
    table_rows=getChildren(driver,"tbody","tr","tag","tag")
    if len(table_rows)==0:
        BuiltIn().log("Unable to extract rows",level="error")
        assert True==False
    result = True
    for  j in range(len(table_rows)):
        columns=getChildren(driver,childrenlocator="td",childrenlocatorType="tag",parent=table_rows[j])
        if len(columns)==0:
            BuiltIn().log("Unable to extract columns in row number "+str(j+1))
            continue
        BuiltIn().log("Number of columns")
        BuiltIn().log("### Company number "+str(j+1)+"###")
        for i in range(len(columns)):
            if table_titles[i]=="Add to Portfolio":
                continue
            elif table_titles[i]=="Pass/Fail":
                number_tries=0
                while (number_tries<5):
                    number_tries+=1
                    pass_fail_text=str(columns[i].text).replace("\n"," ")
                    if pass_fail_text != "":
                        break
                if pass_fail_text =="":
                    BuiltIn().log(table_titles[i]+" is empty in company number "+str(j+1),level="error")
                    result = False
                elif halal:
                    if  ("Pass" not in pass_fail_text) :
                        BuiltIn().log("pass_fail_text has a wrong syntax ===> "+pass_fail_text)
                    else:
                        BuiltIn().log(table_titles[i]+" is not empty and is accurate"+"===>"+pass_fail_text)
                else:
                    if ("Fail" not in pass_fail_text) & ("Pass" not in pass_fail_text) & ("Missing Data" not in pass_fail_text):
                        BuiltIn().log("pass_fail_text has a wrong syntax ===> "+pass_fail_text)
                    else:
                        BuiltIn().log(table_titles[i]+" is not empty and is accurate"+"===>"+pass_fail_text) 
            else: 
                column_text=columns[i].text 
                if column_text !="":
                    BuiltIn().log(table_titles[i]+" is not empty"+"===>"+column_text)
                else:
                    BuiltIn().log(table_titles[i]+" is empty in company number "+str(j+1),level="error")
                    result = False
    return result
   

  