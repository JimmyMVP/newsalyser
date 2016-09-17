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



def extract_sentiment(api_key="87add3c04a657951ee91eee94d11290b8a734750", sites="http://www.cnn.com/2016/09/18/realestate/so-you-think-your-place-is-small.html?hp&action=click&pgtype=Homepage&clickSource=image&module=photo-spot-region&region=top-news&WT.nav=top-news&mtrref=www.nytimes.com&gwh=689DBA02B8BA5664CCFD84935A2030C3&gwt=pay"):
    alchemy_language = AlchemyLanguageV1(api_key = api_key)
    response = {}
    combined_operations = ['page-image','title', 'author', 'taxonomy', 'doc-emotion']

    for curr_site in sites:
        print(curr_site)

        for article in sites[curr_site]:

            curr_url = article["url"]
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
                print("Excpeption")
                continue
            response_dict = json.loads(curr_response)
            
            response_dict["brand"] = curr_site
            response_dict["top_image"] = article["top_image"]

            article_model = Article(title = response_dict["title"], url = response_dict["url"], brand = response_dict["brand"], json =  response_dict, clustered = False)
            article_model.save()

            print("Saved model: " + str(article_model))

            print(response_dict)












