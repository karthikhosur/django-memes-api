from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import spacy
import re


# Create your views here.
@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        url = "https://bing-news-search1.p.rapidapi.com/news"

        querystring = {"setLang": 'EN', "cc": 'US',
                       "safeSearch": "Moderate", "textFormat": "Raw"}

        headers = {
            "X-BingApis-SDK": "true",
            "X-RapidAPI-Key": "4d08172c5amshe7be1524b581b3ep118814jsn1ee9225ee171",
            "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        # print(response.json())
        data = response.json()
        data = data['value']
        news_names = []
        news_urls = []
        for d in data:
            news_names.append(d['name'])
            news_urls.append(d['url'])
            news_urls.append(d['description'])

        nlp = spacy.load("en_core_web_sm")

        s = ' '.join(news_names)
        doc = nlp(s)

        proper_nouns_list = extract_proper_nouns(doc)

        image_urls = get_image_urls(proper_nouns_list)
        print(image_urls)
        return Response({'data': image_urls})


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


def get_image_urls(proper_nouns_list):
    image_urls = []
    for i in range(len(proper_nouns_list)):
        res = re.sub(r'[^a-zA-Z]', '', str(proper_nouns_list[i]))
        if len(res) > 2:
            q = str(proper_nouns_list[i]) + " Memes"

            q = q.replace(" ", "%20")

            url = "https://serpapi.com/search.json?q="+q + \
                "&tbm=isch&ijn=0&api_key=6a264e162a0d9e3ef8b8b0d381a1d38b8b61f6ae7096d61d37c3580394a355a6&tbs=qdr:d"

            payload = {}
            headers = {}

            response = requests.request(
                "GET", url, headers=headers, data=payload)

            results = response.json()
            i = 0
            while i < 10:
                image_urls.append(results['images_results'][i]['original'])
                i += 1
    return image_urls
