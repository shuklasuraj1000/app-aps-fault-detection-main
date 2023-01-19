import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from echa.logger import logging
from echa.exception import ECHAException
import sys


        
def element_ref_link(substance:str)->list:
    """ This funtion search relevent substance link in ECHA website.
        enter substance name, for fast and accurate search enter CAS number if availble.
    """
    substance_name = str(substance)
    logging.info("finding chromedriver exe file for getting REF list")
    service_link = Service
    serv_object = service_link(r"C:\Users\soshukla\Desktop\ECHA\chromedriver_win32\chromedriver.exe")
    driver=webdriver.Chrome(service = serv_object)
    logging.info(driver)
    driver.get("https://echa.europa.eu/")
    time.sleep(2)
    
    try:
        # Click for auto acceptence of legal acceptence of REACH website
        a =driver.find_element(By.CLASS_NAME,"disclaimerIdCheckboxLabel").click()
        
    except Exception as e:
        raise ECHAException (e, sys)

    try:
        driver.find_element(By.ID,"autocompleteKeywordInput").send_keys(substance_name)
        driver.find_element(By.ID,"_disssimplesearchhomepage_WAR_disssearchportlet_searchButton").click()
        
        # After sending seach keyword (Either substance name of CAS number) sleep for 5 seconds
        time.sleep(5)
        urls=driver.find_elements(By.CSS_SELECTOR,'a.substanceNameLink ')
        
        # After fetching all relevent URL link wait for 5 senconds and move to next step.
        time.sleep(5)
        logging.info("urls added successfully")
        
        if len(urls)>0:
            col1=[]
            for url in urls:
                col1.append(url.get_attribute('href'))

        else:
            logging.info("No link found")
            
        logging.info(col1)
        
        # Closing the driver   
        driver.close()
        return col1
    except Exception as e:
        driver.close()
        raise ECHAException(e, sys)
    
def REACH_STATUS(ref:list):

    col1 = ref
    logging.info("finding chromedriver exe file for REACH STATUS CHECK")
    service_link = Service
    serv_object = service_link(r"C:\Users\soshukla\Desktop\ECHA\chromedriver_win32\chromedriver.exe")
    
    substance=[]
    CAS=[]
    comment=[]
    for i in range(3):
        logging.info(f"{'>>'*20} \n Seaching for elemnet number: {i+1}")
        time.sleep(2)
        link=col1[i]
        driver=webdriver.Chrome(service = serv_object)
        driver.get(link)
        time.sleep(10)
        driver.find_element(By.XPATH,"//button[contains(@class,'primaryBTN')]").click()
        time.sleep(2)
        # Capturing substance name
        try:
            d2=driver.find_element(By.XPATH,"//*[@id='substanceIdentifiersContainer']/h2")
            logging.info(d2.text)
            substance.append(d2.text)
        except:
            pass
        
        # Capturing CAS number of substance
        try:
            d1=driver.find_element(By.CLASS_NAME,"separatedCasNumbers")
            logging.info(d1.text)
            CAS.append(d1.text)
        except:
            pass
        
        # Capturing status REACH ANEXX XIV/ XVII impacted or not.
        try:
            time.sleep(2)
            c2=driver.find_element(By.XPATH,"//a[text()='Restriction list']/parent::*/following-sibling::div/div")
            logging.info(c2.text)
            comment.append(c2.text)
            time.sleep(2)
            driver.close()

        except:
            comment.append("No information available")
            time.sleep(2)
            driver.close()
            pass

    df = pd.DataFrame(np.column_stack([substance, CAS, comment ]), columns=['substance','CAS', 'comment'])
    print(df)
    return df
        
