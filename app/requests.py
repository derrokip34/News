import urllib.request,json
from .models import Sources,Articles

api_key = None
sources_url = None
articles_url = None
headlines_url = None

def configure_request(app):
    global api_key,sources_url,articles_url,headlines_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_SOURCES_URL']
    articles_url = app.config['NEWS_ARTICLES_URL']
    headlines_url = app.config['TOP_HEADLINES_URL']

def get_sources(category):

    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_results(get_sources_response['sources'])

    return sources_results

def process_results(new_sources_list):

    news_sources_results = []

    for source in new_sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        if url:
            news_source_object = Sources(id,name,description,url,category,country)
            news_sources_results.append(news_source_object)
    
    return news_sources_results

def get_articles(id):

    get_articles_url = articles_url.format(id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        news_articles_results = None

        if get_articles_response['articles']:
            news_articles_results_list = get_articles_response['articles']
            news_articles_results = process_articles(news_articles_results_list)

    return news_articles_results

def process_articles(news_articles_list):

    news_articles_results = []
    for article_item in news_articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')


        if urlToImage:
            news_articles_object = Articles(id,author,title,description,url,urlToImage,publishedAt)
            news_articles_results.append(news_articles_object)

    return news_articles_results

def get_headlines(limit):

    get_headlines_url = headlines_url.format(limit, api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_articles(headlines_results_list)

    return headlines_results