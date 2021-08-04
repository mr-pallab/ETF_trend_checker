# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:30:27 2021

@author: mahfu
"""
import Parallel_data_acquisition as pda
import operator
from time import time
from datetime import datetime, timedelta
import os

def trend_check(ETFs):
    start = time()
    data = pda.parallel_execution(ETFs)
    print ("Execution time: " + str(round(time()-start,2)) +" seconds")
    
    processed_data = {}
    trend = {}
    for ii in data:
        ETF_name = ii[0]
        max_data = max(ii[1].items(), key=operator.itemgetter(1))
        max_val = max_data[1]
        max_date = max_data[0]
        
        min_data = min(ii[1].items(), key=operator.itemgetter(1))
        min_val = min_data[1]
        min_date = min_data[0]
        
        for dates,value in ii[1].items():
            if dates >= (datetime.today().date() - timedelta(days=1)):
                current_val = ii[1][dates]
                current_date = dates
                
        processed_data[ETF_name]=[max_date,max_val,min_date,min_val,current_date,current_val]
        
        delta_high = ((current_val - max_val)/current_val)*100
        delta_low = ((current_val - min_val)/current_val)*100
        trend_strength = delta_high + delta_low
        if trend_strength > 0:
            trend_text = 'Up'
        else:
            trend_text = 'Down'        
        
        name_text = ii[2]
        trend[ETF_name] = [name_text, trend_text, round(trend_strength,2), round(delta_high,2), round(delta_low,2)]                
        
    return processed_data,trend

if __name__ == '__main__':

    ETFs = ['LU1681045370','IE00BK5BQT80','IE00BK5BQX27','IE00BF4RFH31']
    data,trend = trend_check(ETFs)
    os.system("taskkill /f /im chromedriver.exe")
    print ("=="*35)
    for key,value in trend.items():        
        print ("ETF Ticker       : " + str(key))
        print ("ETF Name         : " + str(value[0]))
        print ("--"*35)
        print ("Current trend    : " + str(value[1]))
        print ("Trend Strength   : " + str(value[2]))
        print ("Difference to Max: " + str(value[3]))
        print ("Difference to Min: " + str(value[4]))
        print ("=="*35)
    