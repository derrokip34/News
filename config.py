import os
class Config:
	NEWS_ARTICLES_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
	NEWS_SOURCES_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
	TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,bloomberg,engadget,espn,fortune,al-jazeera-english,cnn,independent&pageSize={}&apiKey={}'
	NEWS_API_KEY =os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True

config_options = {
	'development':DevConfig,
	'production':ProdConfig
}