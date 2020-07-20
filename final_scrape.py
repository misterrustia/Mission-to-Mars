

# import splt and b4s 
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 



# set the executahble path and initialze
executable_path ={'executable_path':'/usr/local/bin/chromedriver'}
browser = Browser('chrome',**executable_path)


def scrape_all():
    # visit the mars nasa news site
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)



    # Find first link and click it 
    browser.is_element_present_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
    firt_hem_link = browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced')
    firt_hem_link.click()



    #once at first link for first hem need to parse and collect title and image
    html = browser.html
    frst_hem_page = BeautifulSoup(html, 'html.parser')
    first_hem_title = frst_hem_page.find("h2", class_='title').get_text()


    frst_hem_pic = frst_hem_page.select_one('div.downloads a ').get("href")
    frst_hem_pic



    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find second link and click it 
    browser.is_element_present_by_text('Schiaparelli Hemisphere Enhanced', wait_time=1)
    second_hem_link = browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced')
    second_hem_link.click()



    html = browser.html
    second_hem_page = BeautifulSoup(html, 'html.parser')
    second_hem_title = second_hem_page.find("h2", class_='title').get_text()
    second_hem_title



    second_hem_pic = second_hem_page.select_one('div.downloads a ').get("href")
    second_hem_pic


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find link and click it 
    browser.is_element_present_by_text('Syrtis Major Hemisphere Enhanced', wait_time=1)
    second_hem_link = browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced')
    second_hem_link.click()



    html = browser.html
    third_hem_page = BeautifulSoup(html, 'html.parser')
    third_hem_title = third_hem_page.find("h2", class_='title').get_text()
    third_hem_title



    third_hem_pic = third_hem_page.select_one('div.downloads a ').get("href")
    third_hem_pic


    # fourth hem 

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find link and click it 
    browser.is_element_present_by_text('Valles Marineris Hemisphere Enhanced', wait_time=1)
    forth_hem_link = browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced')
    forth_hem_link.click()



    html = browser.html
    forth_hem_page = BeautifulSoup(html, 'html.parser')
    forth_hem_title = forth_hem_page.find("h2", class_='title').get_text()
    forth_hem_title



    forth_hem_pic = forth_hem_page.select_one('div.downloads a ').get("href")
    forth_hem_pic



    browser.quit()

    hem_lst=[
        {"img_url":frst_hem_pic,"title":first_hem_title },
    {"img_url":second_hem_link,"title":second_hem_title},
    {"img_url":third_hem_pic,"title":third_hem_title},
    {"img_url":forth_hem_pic,"title":forth_hem_title}
    ] 
    print(hem_lst)
    
    return hem_lst

    

