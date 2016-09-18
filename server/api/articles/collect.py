import json
from watson_developer_cloud import AlchemyLanguageV1
import datetime
import newspaper
import requests
import pickle


from .models import Article, Cluster
categories = ["Business", "World", "Politics", "Entertainment"]



def get_bingp():
    with open('/Users/Jimmy/Projects/hackzurich/server/api/articles/response_by_categories.pickle', 'rb') as handle:
        b = pickle.load(handle)
        return b


def get_bing(api_key = "***REMOVED***"):

    headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': api_key,
    }

    category = "Business"
    api_url = "https://api.cognitive.microsoft.com/bing/v5.0/news?mkt=en-us&category=$%s" %(category)

    print(api_url)
    resp = requests.get(api_url, headers = headers)

    d = json.loads(resp.text)

    return d



def analyse(json):

    clusters = json["value"]


    for cluster in clusters:


        if(Article.objects.filter(url = cluster["url"]).exists()):
                continue


        #Store alchemy analysis
        if(Cluster.objects.filter(cluster_title = cluster["name"]).exists()):
                continue

        cluster_model = Cluster(cluster_title = cluster["name"], category = cluster["category"])
        cluster_model.save()


        alchemy_analysis = sentiment(site = cluster["url"])
        article_model = Article(title = cluster["name"], category = cluster["category"], url = cluster["url"], brand = cluster["provider"][0]["name"], json=alchemy_analysis, clustered = True, cluster = cluster_model)
        article_model.save()


        try:
            clustered_articles = cluster["clusteredArticles"]
        except Exception as e:
            print(e.args)
            return

        for article in clustered_articles:

            print(article)

            if(Article.objects.filter(url = article["url"]).exists()):
                continue

            alchemy_analysis = sentiment(site = article["url"])

            article_model = Article(title = article["name"], category = article["category"], url = article["url"], brand = article["provider"][0]["name"], json=alchemy_analysis, clustered = True, cluster = cluster_model)
            article_model.save()







def sentiment(api_key="***REMOVED***", site = ""):
    alchemy_language = AlchemyLanguageV1(api_key = api_key)
    response = {}
    combined_operations = ['page-image', 'author', 'taxonomy', 'doc-emotion', 'doc-sentiment']


    curr_url = site
        
    try:
        curr_response = json.dumps(
          alchemy_language.combined (
            url=curr_url,
            extract=combined_operations,
           ),
          indent=2)
    except Exception as e:
        print(e.args)
        return -1

    response_dict = json.loads(curr_response)
    
    print("Sentiment calculated")

    return response_dict




def extract_sentiment(api_key="***REMOVED***", sites="http://www.cnn.com/2016/09/18/realestate/so-you-think-your-place-is-small.html?hp&action=click&pgtype=Homepage&clickSource=image&module=photo-spot-region&region=top-news&WT.nav=top-news&mtrref=www.nytimes.com&gwh=689DBA02B8BA5664CCFD84935A2030C3&gwt=pay"):
    alchemy_language = AlchemyLanguageV1(api_key = api_key)
    response = {}
    combined_operations = ['page-image', 'author', 'taxonomy', 'doc-emotion', 'doc-sentiment']

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












