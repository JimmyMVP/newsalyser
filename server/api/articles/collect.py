import json
from watson_developer_cloud import AlchemyLanguageV1
import datetime
import newspaper

from .models import Article

def scrape(news_sites=[]):

    urlmap = {}
    for site in news_sites:
        news = newspaper.build(site)
        site = news.brand
        urlmap[site] = []
        for article in news.articles:
            urlmap[site].append({"url" : article.url, "top_image" : article.top_image})

    return urlmap

def delete_dict_key(dict,keys):
    for key in keys:
        del dict[key]

#keys = ["status","totalTransactions","keywords","concepts","entities","usage"]

#delete_dict_key(dict_req["json"],keys)

def extract_sentiment(api_key="***REMOVED***", sites="http://www.cnn.com/2016/09/18/realestate/so-you-think-your-place-is-small.html?hp&action=click&pgtype=Homepage&clickSource=image&module=photo-spot-region&region=top-news&WT.nav=top-news&mtrref=www.nytimes.com&gwh=689DBA02B8BA5664CCFD84935A2030C3&gwt=pay"):
    alchemy_language = AlchemyLanguageV1(api_key = api_key)
    response = {}
    combined_operations = ['page-image','title', 'author', 'taxonomy', 'doc-emotion', 'doc-sentiment']

    for curr_site in sites:
        print(curr_site)

        for article in sites[curr_site]:

            curr_url = article["url"]
            print(curr_url)

            if curr_url=="":
                continue

            #Is it in database?
            if(Article.objects.filter(url = curr_url).exists()):
                continue
            try:
                curr_response = json.dumps(
                  alchemy_language.combined (
                    url=curr_url,
                    extract=combined_operations,
                   ),
                  indent=2)
            except Exception as e:
                print(e.args)
                continue
            response_dict = json.loads(curr_response)
            
            response_dict["brand"] = curr_site
            response_dict["top_image"] = article["top_image"]

            title = response_dict["title"]
            del response_dict["title"]

            article_model = Article(title = title, url = response_dict["url"], brand = response_dict["brand"], json =  response_dict, clustered = False)
            article_model.save()

            print("Saved model: " + str(article_model))

            print(response_dict)












