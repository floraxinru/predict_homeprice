#for MVP, give it links for the 6 vancouver pages manually, work with the 120 data points
#then try Seattle page Download All -- * ask about Selenium click

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_binary
import pandas as pd
import numpy as np

#import functions I wrote
from data_dict import make_data_dict

#pages 1-6
van_urls = ["https://www.redfin.ca/bc/greater-vancouver-regional-district/vancouver", "https://www.redfin.ca/bc/greater-vancouver-regional-district/vancouver/page-2", "https://www.redfin.ca/bc/greater-vancouver-regional-district/vancouver/page-3", "https://www.redfin.ca/bc/greater-vancouver-regional-district/vancouver/page-4", "https://www.redfin.ca/bc/greater-vancouver-regional-district/vancouver/page-5", "https://www.redfin.ca/bc/greater-vancouver-regional-district/vancouver/page-6"]
driver = webdriver.Chrome()

data_list = []
url_list = []
for page in van_urls:
    matrix_url = page
    driver.get(matrix_url)
    elements=driver.find_elements_by_partial_link_text("Vancouver, BC")

    for element in elements: 
    #each element is a webelement for that house listed on the page
        data_d = make_data_dict(element.text)  #scrape info of this listing (before going into url for more detail)
        data_list.append(data_d)
        url_list.append(element.get_attribute("href")) #find link for each house listing

        time.sleep(2) #wait 2 seconds
        
    #pull this out into a function?
    #print(len(url_list)) #20 houses per page
    #print(data_list)

df_info20 = pd.DataFrame(data_list)
df_links20 = pd.DataFrame(url_list) #put list of links into dataframe

    #save results of first page into csv:
df_info20.to_csv("info_20.csv", index=False) 

df_links20.to_csv("links_20.csv", index=False) 


#stop 2 sec for each house, started 5:49, 120 houses = pause for 240 seconds, about 5 minutes?
#page 1 took <1min, stayed in same driver window (does it matter?). 5:51 on page 4. 5:54 finished, 5mins
#problem: csv file overwrite, also last page only has 3!

#pull last 4 lines (DF and csv) out of loops, started 5:58, page 4 at 6:00 (faster because not making a csv for each page)
#only 3 houses on page 6, so only 103 listings/links total. Still only getting last page??

#Initialized data and url lists outside of for loops, started: 6:08, finished 6:13

assert "No results found." not in driver.page_source

driver.close()
