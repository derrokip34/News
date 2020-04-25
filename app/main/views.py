from flask import render_template
from . import main
from ..requests import get_sources
from ..models import Sources,Articles

@main.route('/')
def index():

    general_news = get_sources('general')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    business_news = get_sources('business')

    title = 'Welcome to Fro News'

    return render_template('index.html', title = title,general = general_news, entertainment = entertainment_news, sports = sports_news, technology = technology_news, business = business_news)