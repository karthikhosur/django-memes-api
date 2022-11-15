from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import spacy


# Create your views here.
@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        url = "https://bing-news-search1.p.rapidapi.com/news"

        querystring = {"setLang": 'EN', "cc": 'US',"safeSearch":"Moderate","textFormat":"Raw"}

        headers = {
            "X-BingApis-SDK": "true",
            "X-RapidAPI-Key": "4d08172c5amshe7be1524b581b3ep118814jsn1ee9225ee171",
            "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # print(response.json())
        data = response.json()
        data = data['value']
        news_names=[]

        for d in data:
            news_names.append(d['name'])
        # print(news_names)
                

        nlp = spacy.load("en_core_web_sm")


        s = ' '.join(news_names)
        doc = nlp(s)

        proper_nouns_list = extract_proper_nouns(doc)
        print(proper_nouns_list)
        return Response({'data': []})

        
def extract_proper_nouns(doc):
    pos = [tok.i for tok in doc if tok.pos_ == "PROPN"]
    consecutives = []
    current = []
    for elt in pos:
        if len(current) == 0:
            current.append(elt)
        else:
            if current[-1] == elt - 1:
                current.append(elt)
            else:
                consecutives.append(current)
                current = [elt]
    if len(current) != 0:
        consecutives.append(current)
    return [doc[consecutive[0]:consecutive[-1]+1] for consecutive in consecutives]


