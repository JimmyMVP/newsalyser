import json
from watson_developer_cloud import AlchemyLanguageV1
import requests
import  pymongo
from pymongo import MongoClient
import datetime
import newspaper

def scrape(news_sites=[]):

    urlmap = {}
    for site in news_sites:
        news = newspaper.build(site)
        urlmap[site] = []
        for article in news.articles:
            urlmap[site].append(article.url)
    return urlmap



def Extract_Sentiment(api_key="87add3c04a657951ee91eee94d11290b8a734750", sites="http://www.cnn.com/2016/09/18/realestate/so-you-think-your-place-is-small.html?hp&action=click&pgtype=Homepage&clickSource=image&module=photo-spot-region&region=top-news&WT.nav=top-news&mtrref=www.nytimes.com&gwh=689DBA02B8BA5664CCFD84935A2030C3&gwt=pay"):
    alchemy_language = AlchemyLanguageV1(api_key = api_key)
    response = {}
    combined_operations = ['page-image', 'entity', 'keyword', 'title', 'author', 'taxonomy', 'concept', 'doc-emotion']
    for curr_site in sites:
        print(curr_site)

        for curr_url in sites[curr_site]:
            print(curr_url)
            if curr_url=="":
                continue
            try:
                curr_response = json.dumps(
                  alchemy_language.combined (
                    url=curr_url,
                    extract=combined_operations,
                   ),
                  indent=2)
            except:
                print("excpeption")
                continue
            respones_dict = json.loads(curr_response)
            print(respones_dict)
            response[respones_dict["url"]] = respones_dict

    print(response)

sites  = ["http://www.usatoday.com/","http://www.dailymail.co.uk/home/index.html","https://www.yahoo.com/news/?ref=gs","https://www.theguardian.com/world","http://en.canoe.com/home.html","http://edition.cnn.com/WORLD/","http://www.theage.com.au/","http://www.journalgazette.net/","http://washingtonpost.com/","http://www.nytimes.com/","http://foxnews.com/","http://bbc.com/","http://www.111breakingnews.com/?f"]
srcs = scrape(sites)
print(srcs)
print("*********************************************")
Extract_Sentiment(sites = srcs)