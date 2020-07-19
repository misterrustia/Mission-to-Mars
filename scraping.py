
# import splt and b4s 
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import datetime as dt


# set the executahble path and initialze
executable_path ={'executable_path':'/usr/local/bin/chromedriver'}

def scrape_all():
        #initiate headless driver for deployment 
    browser = Browser('chrome',executable_path ="chromedriver", headless = False)

    news_title, News_paragraph = mars_news(browser)

    #run all scrapping functions and store results in a dicitionary 
    data ={
        "news_title": news_title,
        "news_paragraph": News_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }


    # stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
    # visit the mars nasa news site
    url = 'http://mars.nasa.gov/news/'
    browser.visit(url)
    # optional delay for loading the page 
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    #searching for elements with specific combination of tag(ul and li )
    #xmple = ul.item_list == <ulclass="item_list">

    # secondly we are telling our browser to wait one second before searching for c
    #components to give more time to load if they are image heavy


    #after check( is element present by css) booleen = true
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')

    # we have set slide_elem as element to look for the ul tag and the li inside of it
    # the . is used to search class such as itme_list 



    # Notice how we’ve assigned slide_elem as the variable to 
    # look for the <ul /> tag and its descendent (the other tags within the <ul /> element),
    # the <li /> tags? This is our parent element. This means that this
    # element holds all of the other elements within it, 
    # and we’ll reference it when we want to filter search
    # results even further. The . is used for selecting classes,
    # such as item_list, so the code 'ul.item_list li.slide'
    # pinpoints the <li /> tag with the class of slide and 
    # the <ul /> tag with a class of item_list. 
    # CSS works from right to left, such as returning the last
    # item on the list instead of the first. Because of this, 
    # when using select_one, the first matching element returned 
    # will be a <li /> element with a class of slide and all nested
    # elements within it.

    # add try /except for error handling 
    try:
        # assin tittle and summary text to variables
        slide_elem.find("div", class_='content_title')
        # chainging .find method here looks inside slide_elem for div class= content title



        #use the parent elementy to find the first "a" tag and save it as "news title"
        news_title=slide_elem.find("div", class_='content_title').get_text()
        #print(news_title)


        # steps 1 identify parent element and create variable to hold it 
        # 2 with new line search withing for title 
        # 3 stripp additional html and tags with .get_text()


        news_p=slide_elem.find("div", class_='article_teaser_body').get_text()
        #print(news_p)

        # There are two methods used to find tags and attributes with BeautifulSoup:
        # 
        # .find() is used when we want only the first class and attribute we’ve 
        # specified.
        # .find_all() is used when we want to retrieve all of the tags and 
        # attributes.
        # For example, if we were to use .find_all() instead of .find() when
        # pulling the 
        # summary, we would retrieve all of the summaries on the page instead of
        # just the first one.

        # ### Featered Images 
    except AttributeError:
        # if attribute error found return nothing instead 
        print("Attribute error")
        return None, None

    return news_title, news_p

def featured_image(browser):
    
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    # This is significant because in HTML, 
    # an id is a completely unique identifier.
    # An id, on the other hand, can only be used one time
    # throughout the entire page.
    # 


    # have splinter(browser use fnc find by id = full image)
    full_image_elem = browser.find_by_id('full_image')
    #use click func on object 
    full_image_elem.click()


    # have splinter search the page by text to find more info button as 
    # no id to be used to find button in html 
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()


    #parse the resulting html with soup 
    html = browser.html 
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
            
        # we dont want just the specific image there we want what ever the newst is 
        # as it is updated , need code to be flexible 
        # find the relative image url 
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
        img_url_rel
        # using select one from parsed html , <a> img and figure.lede = class lede
        #.get src fnc pulls image link 


        # What we’ve done here is tell BeautifulSoup to look inside 
        # the <figure class=”lede” /> tag for an <a /> tag, and then
        # look within that <a /> tag for an <img /> tag. Basically we’re 
        # saying, “This is where the image we want lives—use the link that’s inside
        # these tags.”



        # # start 10.3.5 
        # # extract ables by tags to be placed in application 
        # instead of scraping each row of the data in the table we wil use 
        # pandas .read_html() fnc 
    except AttributeError:
        print("Attribute error")
        return None
    
    # link is missng url need to add 
    # use base url to create aosolute url
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    
    return img_url

def mars_facts():
    try:
        df = pd.read_html('http://space-facts.com/mars/')[0]
        #only pull first table encountered on page and make it into a df 
        df.columns=['description','value']
        df.set_index('description', inplace=True)
        # the inplace makes it so we dont need to make a new df variable 
        #df
        #did we need splinter to do this or no ? or did pandas navigate to the page it self ?


    except BaseException:
        return None

    return df.to_html()
    
        #pandas can set up the table to be put back onto the web !!! 



if __name__ =="__main__":
    # if running as script, print scraped data
    print(scrape_all())

