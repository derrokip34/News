class Config:
	NEWS_ARTICLES_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
	NEWS_SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
	NEWS_API_KEY = '72de9031f1ba459ea277cf92829e78e5'

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True

config_options = {
	'development':DevConfig,
	'production':ProdConfig
}