# ETF_trend_checker
The files in this repository contains a set of practice scripts which incrementally implement analysis of ETFs based on interactive charts available on JustETF.com.
No APIs are used to fetch the data, rather using Selenium in Python, the data is directly scraped from the webpage.

Steps implemented so far:

1. ETF_trend_checker.py contains the function to fetch the data of a particular ETF for the last 1 month (daily price)
2. Parallel_data_acquisition.py contains implementation of multiprocessing module method (Pool) to parallellize acquisiton of data for multiple ETFs.
3. Analysis.py provides functionality to perform trend analysis based on data fetched with the help of the previous modules.

Steps remaining:
1. Refinement of Parallel_data_acquisition.py script.
2. Further refinements in exception handling, edge cases and general improvements.
3. extension of trend analysis to take into account all data point rather than just Max and Min.

Developed by: Mahfuzur Rahman (pallab86@gmail.com)
