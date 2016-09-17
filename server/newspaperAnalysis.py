import json
from watson_developer_cloud import AlchemyLanguageV1
import requests
import  pymongo
from pymongo import MongoClient
import datetime
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
db = client['test-database']
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
       "date": datetime.datetime.utcnow()}

def Extract_Sentiment(api_key="87add3c04a657951ee91eee94d11290b8a734750", urls="http://www.cnn.com/2016/09/18/realestate/so-you-think-your-place-is-small.html?hp&action=click&pgtype=Homepage&clickSource=image&module=photo-spot-region&region=top-news&WT.nav=top-news&mtrref=www.nytimes.com&gwh=689DBA02B8BA5664CCFD84935A2030C3&gwt=pay"):
    alchemy_language = AlchemyLanguageV1(api_key = api_key)
    response = {}
    combined_operations = ['page-image', 'entity', 'keyword', 'title', 'author', 'taxonomy', 'concept', 'doc-emotion']
    for curr_url in urls:
        curr_response = json.dumps(
          alchemy_language.combined (
            url=curr_url,
            extract=combined_operations,
           ),
          indent=2)

        respones_dict = json.loads(curr_response)

        response[respones_dict["url"]] = respones_dict

        print(curr_response)
Extract_Sentiment(urls =[ "http://www.msn.com/en-us/news/us/two-police-officers-shot-in-philadelphia/ar-BBwgf79?li=BBnb7Kz"])