# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 00:11:31 2021

@author: Mahfuzur Rahman
"""
import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime as dt

folder = os.getcwd()
options = Options()
options.add_argument('--headless')
options.add_argument('--start-maximized')

driver = webdriver.Chrome(folder+'//chromedriver.exe', options=options)

def get_etf_data(ETF):

    print ("Now checking prices of the "+ ETF +" ETF")    
    URL = 'https://www.justetf.com/en/etf-profile.html?query='+ETF+'&groupField=index&from=search&isin='+ETF+'#chart'

    driver.get(URL)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"]').click()


    driver.find_element_by_xpath("//a[@title='1 month']").click()

    select = Select(driver.find_element_by_xpath("//*[@name='chartPanel:chart:content:optionsPanel:selectContainer:valueType']"))
    select.select_by_visible_text('Market Value')
    
    select = Select(driver.find_element_by_xpath("//*[@name='chartPanel:chart:content:optionsPanel:selectContainer:currencies']"))
    select.select_by_visible_text('EUR')

    time.sleep(1)
   
    ETF_name = (driver.find_element_by_xpath(".//*[contains(text(),'Performance chart of ')]").text).replace("Performance chart of ","")
    
    graph = driver.find_element_by_xpath("//div[@class='chartoptions']/following-sibling::div")
    chart_size =  graph.size

    margin = 10
    x_limit = int(chart_size['width']/2) - margin

    time.sleep(1)

    data = {}
    action = AC(driver)
    hover = action.move_to_element(graph)

    for i in range (31):   
        if i == 0:
            latest = action.move_by_offset(x_limit,0)        
            latest.perform()
        else:        
            latest = action.move_by_offset(-int(chart_size['width']/30),0)
            latest.perform()

        tooltip_box = driver.find_element_by_class_name('highcharts-tooltip')
        date = tooltip_box.find_element_by_xpath("//*[@style='font-size: 10px;']")
        value = tooltip_box.find_element_by_xpath("//*[@style='font-weight:bold']")
        
               
        # Process date values
        date_processed = dt.strptime(date.text, "%d.%m.%Y").date()
        # Convert value to float, put all data in a dictionary
        if value.text != '':
            data[date_processed]=float(value.text)
            print (str(date_processed) +" : "+ value.text) 

    driver.quit()
    return [ETF, data, ETF_name]

if __name__ == '__main__':
    ETF = 'LU1681045370'
    data_1 = get_etf_data(ETF)