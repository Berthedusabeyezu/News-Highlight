
from app import app
import urllib.request,json
from .models import news
from .models import articles



# Getting api key
api_key = app.config['NEWS_API_KEY']
# api_key = app.config['ARTICLES_API_KEY']


# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
base_url2 = app.config["ARTICLES_API_BASE_URL"]

Articles = articles.Articles
News = news.News

def get_news(category): 
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['sources']:
            new_results_list = get_news_response['sources']
            new_results = process_results(new_results_list)


    return new_results

def process_results(new_list):
    '''
    Function  that processes the new result and transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain new details

    Returns :
        new_results: A list of new objects
    '''
    new_results = []
    for new_item in new_list:
        id = new_item.get('id')
        name = new_item.get('name')
        description = new_item.get('description')
        url = new_item.get('url')
        category = new_item.get('category')
        language = new_item.get('language')
        

        if id:
            new_object = News(id,name,description,url,category,language)
            new_results.append(new_object)

    return new_results
   


def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = base_url2.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        articles_results = None

        if get_article_response['articles']:
            articles_results_list = get_article_response['articles']
            articles_results = process_articles_results(articles_results_list)


    return articles_results


def process_articles_results(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        author = articles_item.get('author')
        title = articles_item.get('title')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')

        articles_object = Articles(id,author,title,url,urlToImage,publishedAt,content)
        articles_results.append(articles_object)

    return articles_results