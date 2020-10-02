from NEWS_FLASK import main_functions
import requests

class news_info():

    def get_news(url_country):
        url_country
        url = ('https://newsapi.org/v2/top-headlines?country=')
        url_api = '&apiKey=ba2f4cd4830c446daed332a6daa22afe'
        url3 = url + url_country + url_api
        response = requests.get(url3).json()

        main_functions.save_to_file(response, "NEWS_FLASK/JSON_FILES/news.json")
        post_index = main_functions.read_from_file("NEWS_FLASK/JSON_FILES/news.json")
        posts = post_index['articles']
        main_functions.save_to_file(posts, "NEWS_FLASK/JSON_FILES/news_title.json")
        total = int(post_index['totalResults'])

        return posts