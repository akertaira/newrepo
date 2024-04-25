from django.shortcuts import render
import requests


def index(request):
    return render(request, 'news/index.html')


def get_news(request, category):
    api_key = '64df44ab696d4a808d5c5cb0e045d7f2'
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        context = {'articles': articles}
    else:
        context = {'error': 'Failed to fetch news'}
    return render(request, 'news/news_list.html', context)
