import requests
import re


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
            print(image_urls)
    return image_urls


get_image_urls(["Senate Leading Republicans", "Trump", "McConnell"])
