from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getElementList,getChildren
import random


def getHeader(driver):
    try:
        table_titles=[]
        table_titles_elements=getChildren(driver,parentlocator="thead",parentlocatorType="tag",childrenlocator="th",childrenlocatorType="tag")
        table_titles_elements.pop(-1)
        for e in table_titles_elements:
            table_titles.append(e.text)
    except:
        table_titles=["Symbol","Price","Change","Change %","Quantity"]
        BuiltIn().log("Unable to extract the header of the portfolio")
    return table_titles

def getQuantityIndexAndLastElementIndex():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    table_titles=getHeader(driver)
    for i in range(len(table_titles)):
        if table_titles[i].lower() == "quantity":
            return [i+1,len(table_titles)+1]

def getRandomQuantity(old_qte):
    while True:
        new_qte=random.randint(0,100)
        if new_qte != old_qte:
            break
    return unicode(new_qte)





def verifyMyPortfolioNotEmpty():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    table_titles=getHeader(driver)
    try:
        row_list=getElementList(driver,locator="tr",locatorType="tag")
    except:
        empty=True
        BuiltIn().log("Can not extract rows",level="error")
    if len(row_list) !=0:
        BuiltIn().log("Number of elements in portfolio: "+str(len(row_list)))
        i=1
        empty=False
        for row in row_list :
            try:
                column_liste=getChildren(driver,childrenlocator="td",childrenlocatorType="tag",parent=row)
            except:
                BuiltIn().log("Can not extract columns in row number "+str(i))
            if len(column_liste)!=0:
                column_liste.pop(-1)
                j=0
                for column in column_liste:
                    if column.text=="":
                        empty=True
                        BuiltIn().log("********Company "+str(i)+"*********")
                        try:
                            BuiltIn().log(table_titles[j]+" is empty")
                        except:
                            BuiltIn().log("A column in this list is empty")
                    j+=1    
                i+=1
            else:
                empty=True
                BuiltIn().log("No columns found in row number "+str(i))
                i+=1
    else:
        empty=True
        BuiltIn().log("No rows found",level="error")
    if empty:
        BuiltIn().log("Some items are missing in the portfolio",level="error")
    else:
        BuiltIn().log("All items are accurate in the portfolio")
    assert empty==False



def VerifyPortfloioDontContainRepeatedRows():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    try: 
        row_list=getElementList(driver,locator="tr",locatorType="tag")
        i=1
        repeated=False
        company_dictionnary=dict()
        for row in row_list :
            column_liste=getChildren(driver,childrenlocator="td",childrenlocatorType="tag",parent=row)
            company_name=str(column_liste[0].text)
            if company_name in company_dictionnary:
                company_dictionnary[company_name]=-1
                repeated=True
            else:
                company_dictionnary[company_name]=i
            i+=1
    except:
        BuiltIn().log("A problem accured while verifying there's no repetetion")
    if repeated :
        BuiltIn().log("The portfolio contains repeated rows",level="error")
    for key,value in company_dictionnary.items():
        if value==-1:
            BuiltIn().log("The company "+key+"is repeated in the portfolio")
    assert repeated==False

           


        

    


