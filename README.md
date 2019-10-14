# project02
Web scraping and regression project: Predicing Home Prices in Vancouver and Seattle
(Metis Data Science Bootcamp, Project 02)

### Introduction

Seattle and Vancouver both offer temperate climate, locations on the Pacific Coast, as well as active lifestyles. They also attract a similar demographic. Having lived in both cities, I'm interested in predicting and comparing their home prices, given a set of features such as home type, number of bedrooms, etc.

Potential clients: Homebuyers looking to relocate to either Vancouver or Seattle, or people looking to invest in real estate in either of the two cities.

### Data
I used a combination of web-scraped data and downloaded flat files. The Vancouver dataset was scraped from redfin.ca, and the Seattle dataset was downloaded from redfin.com. They were the latest data available on their website during the first week of October 2019. The two websites differ slightly in their designs. The two datasets combined have about 450 observations (rows) and 27 unique features (columns). 
For the analysis as of mid-October 2019, I focused on 5 numerical features (price, size in square feet, number of bedrooms, number of bathrooms, and days listed on the market).

### Tools

Python, Pandas, NumPy, Scikit-learn, Seaborn 
HTML, Selenium

### Code
project_model is the main Jupyter Notebook for the project

scrape_van_20for6.py and data_dict.py are codes used for web scraping

### Future Work
My ultimate goal for this project is to develop a web API that potential homebuyers could use to compare home prices in two different cities, after selecting a particular set of filters (2 bed 2 bath, with garage and balcony, for example). 

Next Steps:

- Examine underlying bias in data
- Get more data from different sources
- More feature engineering
- Compare coefficients of each feature using improved model
