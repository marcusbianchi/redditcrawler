#!/usr/bin/python3 
from crawler import crawler
import sys
import pprint

pp = pprint.PrettyPrinter(indent=2)

#my_url = 'https://www.reddit.com/r/worldnews/top/?sort=top&t=day'

def main(arg,main=True):
    result=[]
    urls = arg.split(';')
    for url in urls:
        #get the reddits top of the current day
        url="https://www.reddit.com"+url+"/top/?sort=top&t=day"
        cur_result = crawler.get_data(url)
        if(cur_result!=None):
            result.extend(cur_result)   
    if(main):
        for item in result:
            pp.pprint(item)
    return result

if __name__ == "__main__":
    if(len(sys.argv)==2):
        main(sys.argv[1])