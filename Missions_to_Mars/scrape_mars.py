#!/usr/bin/env python
# coding: utf-8

# In[97]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[98]:


def scrape_info():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Get the latest News Title
    news_title = soup.find('div', class_='content_title').text
    
    # Get the latest news paragraph
    news_p = soup.find('div', class_='article_teaser_body').text
    
    data = {
        "news_title": news_title,
        "news_p": news_p
    }
    
    browser.quit()
    
    return data


# In[99]:


def scrape_info_2():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Get the feature image source
    featured_image_url = soup.find('img', class_='headerimage fade-in')['src']
    complete_url = url + featured_image_url
    
    browser.quit()
    
    return complete_url


# In[100]:


def scrape_table():
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    new_table = tables[0]
    new_table.columns=['Mars - Earth Comparison','Mars', 'Earth']
    new_table.set_index('Mars - Earth Comparison', inplace=True)
    df = new_table.iloc[1: , :]
    html_table = df.to_html()
    
    html_table = html_table.replace('\n', ' ')
    
    return html_table


# In[101]:


def scrape_info_3():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = "https://marshemispheres.com/"
    browser.visit(url)

    time.sleep(1)
    

    xpath = '//*[@id="product-section"]/div[2]/div[1]/div/a/h3'
    xpath2 = '//*[@id="product-section"]/div[2]/div[2]/div/a/h3'
    xpath3 = '//*[@id="product-section"]/div[2]/div[3]/div/a/h3'
    xpath4 = '//*[@id="product-section"]/div[2]/div[4]/div/a/h3'
    info_dict = []
    xpath_list = [xpath, xpath2, xpath3, xpath4]
    
    for x in xpath_list:
        results = browser.find_by_xpath(x)
        click = results[0]
        click.click()

        html = browser.html
        soup = bs(html, "html.parser")

        hemi_title = soup.find('h2', class_='title').text
        full_image = soup.find('img', class_='wide-image')['src']
        full_image_url = url + full_image
        
        data = {
            "title": hemi_title,
            "img_url": full_image_url
        }
        info_dict.append(data)
        browser.back()

    
    browser.quit()
    
    return info_dict


# In[104]:


def complete_scrape():
    
    first_scrape = scrape_info()
    second_scrape = scrape_info_2()
    third_scrape = scrape_table()
    fourth_scrape = scrape_info_3()
    
    result = {
        'latest_news': first_scrape,
        'featured_img': second_scrape,
        'table_html': third_scrape,
        'hemi_data': fourth_scrape
    }
    
    return result
    


# In[105]:





# In[ ]:




