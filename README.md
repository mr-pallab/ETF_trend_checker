# ETF_trend_checker
The files in this repository contains a set of practice scripts which incrementally implement analysis of ETFs based on interactive charts available on JustETF.com.
No APIs are used to fetch the data, rather using Selenium in Python, the data is directly scraped from the webpage.

Steps implemented so far:

1. ETF_trend_checker.py contains the function to fetch the data of a particular ETF for the last 1 month (daily price)
2. Parallel_data_acquisition.py contains implementation of multiprocessing module method (Pool) to parallellize acquisiton of data for multiple ETFs.

Steps remaining:
1. Refinement of Parallel_data_acquisition.py script.
2. Implementation of actual trend analysis based on a custom-defined algorithm in a new script.
3. Further refinements


Developed by: Mahfuzur Rahman (pallab86@gmail.com)
