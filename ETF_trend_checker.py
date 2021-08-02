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
#from multiprocessing import Process
import time

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


    #graph = driver.find_element_by_xpath('//*[@id="highcharts-7juqvl8-387"]/svg/g[9]/g[1]/path[5]')
    #graph = driver.find_element_by_class_name('highcharts-tracker-line')
    #data = graph.get_attribute('d')

    time.sleep(1)
    graph = driver.find_element_by_xpath("//div[@class='chartoptions']/following-sibling::div")
    #chart_area = graph.get_attribute('class')
    #chart_location = graph.location
    chart_size =  graph.size

    margin = 10
    x_limit = int(chart_size['width']/2) - margin
    #y_limit = int(chart_size['height']/2) - margin

    time.sleep(1)

    data = {}
    action = AC(driver)
    hover = action.move_to_element(graph)

    #start = time.time()

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
    
        print (date.text +" : "+ value.text)
        # Put all data in a dictionary
        data[date.text]=value.text

    #extraction_time = time.time() - start
    #print ("Time for data extraction: " + str(round(extraction_time,2)) + " seconds.")

    driver.quit()
    return [ETF, data]

if __name__ == '__main__':
    ETF = 'LU1681045370'
    data_1 = get_etf_data(ETF)