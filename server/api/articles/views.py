from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from . import collect as nlp_collect
from .models import Article


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def root(request, format=None):
    content = {'user_count': "hello"}
    return Response(content)



@api_view(['GET'])
def collect(request, format=None):
    content = "Collected data"

    print("Collecting the data...")
    sites  = ["http://www.usatoday.com/","http://www.dailymail.co.uk/home/index.html","https://www.yahoo.com/news/?ref=gs","https://www.theguardian.com/world","http://en.canoe.com/home.html","http://edition.cnn.com/WORLD/","http://www.theage.com.au/","http://www.journalgazette.net/","http://washingtonpost.com/","http://www.nytimes.com/","http://foxnews.com/","http://bbc.com/","http://www.111breakingnews.com/?f"]
    srcs = nlp_collect.scrape(sites)
    print(srcs)
    print("Collected number: %d" %(len(srcs.keys())) )

    nlp_collect.extract_sentiment(sites = srcs)

    return Response(content)



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def random(request, format=None):

    print("Issuing random article...")
    articles = Article.objects.order_by("added").values()

    return Response(articles[0])
