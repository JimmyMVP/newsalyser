from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from . import collect as nlp_collect
from .models import Article,Cluster

import json



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def root(request, format=None):
    content = {'user_count': "hello"}
    return Response(content)



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_cluster(request, format=None):
    content = {'user_count': "hello"}
    return Response(content)




@api_view(['GET'])
def collect(request, format=None):
    content = "Collected data"

    print("Collecting the data...")

    json = nlp_collect.get_bingp()
    for category in json:
        nlp_collect.analyse(json[category])
    

    return Response(content)




@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def random(request, format=None):

    print("Issuing random article...")
    articles = Article.objects.order_by("added").values()

    return Response(articles[0], headers = {"Access-Control-Allow-Origin" : "*"})




@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def clusters(request, format=None):

    print("Issuing clusters...")

    print("Request" + str(request.body))
    attribute_preferences = json.loads(request.body.decode("utf-8"))

    clusters = Cluster.objects.values()

    if("category" in attribute_preferences):
        clusters = clusters.filter(cateogory = attribute_preferences["category"])
    if("num" in attribute_preferences):
        clusters = clusters[:int(attribute_preferences["num"])]
    
    if len(clusters) == 0:
        return Response({"empty" : True})

    return Response(clusters)



#
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def specific(request, format=None):

    print("Issuing specific articles...")

    print("Request" + str(request.body))
    attribute_preferences = json.loads(request.body.decode("utf-8"))

    articles = Article.objects.order_by("added").values()

    if("num" in attribute_preferences):
        articles = articles[:int(attribute_preferences["num"])]
    if("cateogory" in attribute_preferences):
        articles = articles.filter(cateogory = attribute_preferences["category"])
    if len(articles) == 0:
        return Response({"empty" : True})

    return Response(articles)










