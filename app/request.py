
from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

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
   
def get_sources(id): 
    get_sources_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        sources_details_data = url.read()
        sources_details_response = json.loads(sources_details_data)

        sources_object = None
        if sources_details_response:
            id = sources_details_response.get('id')
            name = sources_details_response.get('name')
            description = sources_details_response.get('description')
            url = sources_details_response.get('url')
            category = sources_details_response.get('category')
            language = sources_details_response.get('language')

            sources_object = News(id,name,name,url,category,language)

    return sources_object