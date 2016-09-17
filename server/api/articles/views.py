from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def root(request, format=None):
    content = {'user_count': "hello"}
    return Response(content)