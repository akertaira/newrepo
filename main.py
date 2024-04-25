import requests
API = '64df44ab696d4a808d5c5cb0e045d7f2'


def extract_news(category):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        for article in articles:
            title = article.get('title', '')
            content = article.get('content', '')
            published_at = article.get('publishedAt', '')
            print(f'Title: {title}\nContent: {content}\nPublished at: {published_at}\n')
    else:
        print(f'Failed to fetch news for category {category}')


extract_news('sports')

