from robot.libraries.BuiltIn import BuiltIn
import sys
import os
dir_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+os.sep +os.pardir)+os.sep+"Base"
sys.path.append(dir_path)
from  Selenium_Driver import getChildren,getElement
import random

def getPriceIndex(driver):
    try:
        table_titles_elements=getChildren(driver,parentlocator="thead",parentlocatorType="tag",childrenlocator="th",childrenlocatorType="tag")
        for i in range(len(table_titles_elements)):
            title=table_titles_elements[i].text
            if title=="Price":
                return i
    except:
        return 4

def getAllPrices():
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    table_rows=getChildren(driver,"tbody","tr","tag","tag")
    if len(table_rows)==0:
        BuiltIn().log("Unable to extract rows",level="error")
        assert True==False
    prices=[]
    for  j in range(len(table_rows)):
        columns=getChildren(driver,childrenlocator="td",childrenlocatorType="tag",parent=table_rows[j])
        if len(columns)==0:
            BuiltIn().log("Unable to extract columns in row number "+str(j+1))
            continue
        price_index=getPriceIndex(driver)
        price=columns[price_index].text
        if price=="":
            BuiltIn().log("Price is empty in company number "+str(j+1),level="error")
        else:
            prices.append(price)
    return prices



def compare(drop_down_item,price,chosen_price):
    if drop_down_item.lower()=="greater than":
        return float(price)>=float(chosen_price)
    elif drop_down_item.lower()=="equal":
        return float(price)==float(chosen_price)
    elif drop_down_item.lower()=="less than" :
        return float(price)<=float(chosen_price)

def priceVerification(drop_down_item,random_price):
    se2lib = BuiltIn().get_library_instance("Selenium2Library")
    driver = se2lib._current_browser()
    table_rows=getChildren(driver,"tbody","tr","tag","tag")
    if len(table_rows)==0:
        BuiltIn().log("Unable to extract rows ===> No rows found with the givin price",level="error")
        assert True==False
    result = True
    for  j in range(len(table_rows)):
        columns=getChildren(driver,childrenlocator="td",childrenlocatorType="tag",parent=table_rows[j])
        if len(columns)==0:
            BuiltIn().log("Unable to extract columns in row number "+str(j+1))
            continue
        price_index=getPriceIndex(driver)
        price=columns[price_index].text
        if price=="":
            BuiltIn().log("Price is empty in company number "+str(j+1),level="error")
            result = False
        else:
            if compare(drop_down_item,price,random_price):
                BuiltIn().log("Price in row "+str(j+1)+" is accurate ==>"+price)
            else:
                BuiltIn().log("Price in row "+str(j+1)+" is not accurate ==>"+price,level="error")
                result = False
    return result





    






