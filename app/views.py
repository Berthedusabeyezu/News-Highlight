from flask import render_template
from app import app
from .request import get_news

 
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

@app.route('/new/<int:id>')
def new(id):

    '''
    View new page function that returns the new details page and its data
    '''
    new = get_new(id)
    title = f'{new.title}'

    return render_template('new.html',title = title,movie = new)