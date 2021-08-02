# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:09:22 2021

@author: mahfu
"""
#from multiprocessing import Pool
import multiprocessing as mp
import ETF_trend_checker as get_ETF

#ETFs = ['LU1681045370','IE00BK5BQT80','IE00BK5BQX27']


def parallel_execution(ETFs):
    number_of_processes = len(ETFs)
    results = mp.Pool(number_of_processes).map(get_ETF.get_etf_data, ETFs)
    outputs = [result for result in results]
    return outputs

if __name__ == '__main__':
    ETFs = ['LU1681045370','IE00BK5BQT80','IE00BK5BQX27']
    #with Pool(len(ETFs)) as p:
    #    data = p.map(get_ETF, ETFs)
    number_of_processes = len(ETFs)
    results = mp.Pool(number_of_processes).map(get_ETF.get_etf_data, ETFs)
    outputs = [result for result in results]
    