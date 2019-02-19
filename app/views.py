from flask import render_template
from app import app
from .request import get_news
from .request import get_article



 
@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)

# Views  
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting popular new
    category_news = get_news('general')
    print(category_news)
    business_news = get_news('business')
    sports_news = get_news('sports')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, general = category_news, business = business_news, sports = sports_news)

@app.route('/new/<id>')
def new(id):

    '''
    View new page function that returns the new details page and its data
    '''
    articles = get_article(id)
    

    return render_template('new.html',articles = articles)
