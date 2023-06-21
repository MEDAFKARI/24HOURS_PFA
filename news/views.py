import requests
import json 
from django.shortcuts import render
from .models import articles, categories

def import_articles():
    url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=bd4cea056d094a9fafe6fe9192d8e4a1"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to retrieve articles from the News API")

    data = response.json()


    for article_data in data["articles"]:
        article = articles()
        article.title = article_data["title"]
        article.desc = article_data["description"]
        article.content = article_data["content"]
        article.image = article_data["urlToImage"]
        article.category = categories.objects.get(name="News")
        article.save()



    


