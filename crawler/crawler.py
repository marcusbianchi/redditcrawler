#!/usr/bin/python3 
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from  urllib.error import HTTPError 
import re
import time 

def get_data(url):  
    try:
        uClient = uReq(url)
        page_html  = uClient.read()
        uClient.close()
        page_soup = soup(page_html,"html.parser")
        site_table = page_soup.findAll("div",{"id":"siteTable"})[0]
        results = []
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
    except HTTPError as e: 
        print(e)
        if e.code == 429:
            time.sleep(3)
            return get_data(url)
        return 
    except IndexError as e: 
        #print(e)
        time.sleep(3)
        return  get_data(url)
    except KeyError as e: 
        #print(e)
        return
