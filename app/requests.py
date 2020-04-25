import urllib.request,json
from .models import Sources,Articles

api_key = None
sources_url = None
articles_url = None

def configure_request(app):
    global api_key,sources_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_SOURCES_URL']
    articles_url = app.config['NEWS_ARTICLES_URL']

