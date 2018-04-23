#!/usr/bin/python3 
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from  urllib.error import HTTPError 
import re
import time 

def get_data(url):  
    try:
        uClient = uReq(url)
        # Get the HTML from the page
        page_html  = uClient.read()
        uClient.close()
        #Transforme into object
        page_soup = soup(page_html,"html.parser")
        #Get the site content table
        site_table = page_soup.findAll("div",{"id":"siteTable"})[0]
        results = []
        #collect the results and save it in form of a Dict
        for item in site_table.select("div[class*=thing]"):
            if(int(item["data-score"])>=5000):
                reddit_thread = {}
                reddit_thread["subreddit"] = item["data-subreddit-prefixed"]
                reddit_thread["upvotes"] = item["data-score"]
                reddit_thread["title"] = item.select("p[class*=title]")[0].a.contents[0]   
                reddit_thread["comments"] = item["data-permalink"]   
                reddit_thread["link"] = item["data-url"]   
                results.append(reddit_thread)
        return results
    # Retry or abort depending on the HTTP error
    except HTTPError as e: 
        print(e)
        if e.code == 429:
            time.sleep(1)
            return get_data(url)
        return 
    # Retry in case of wrong page
    except IndexError as e: 
        #print(e)
        time.sleep(1)
        return  get_data(url)
    # Abort in case of wrong page
    except KeyError as e: 
        #print(e)
        return
