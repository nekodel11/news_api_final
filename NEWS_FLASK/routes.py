import requests
from flask import request, render_template, url_for, redirect
from NEWS_FLASK import app, newsGenerator, main_functions, countryForm


@app.route('/',methods=[ 'GET', 'POST' ])
def index():
    url = 'https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=ba2f4cd4830c446daed332a6daa22afe'
    response = requests.get(url).json()

    main_functions.save_to_file(response, "NEWS_FLASK/JSON_FILES/google_news.json")
    keyword_index = main_functions.read_from_file("NEWS_FLASK/JSON_FILES/google_news.json")
    keyword_posts = keyword_index['articles']
    main_functions.save_to_file(keyword_posts, "NEWS_FLASK/JSON_FILES/google_news.json")
    news_keyword_index = main_functions.read_from_file("NEWS_FLASK/JSON_FILES/google_news.json")

    for i in range(4):
        title = news_keyword_index[i]['title']
    for i in range(4):
        author = news_keyword_index[i]['author']
    for i in range(4):
        source = news_keyword_index[i]['source']['name']
    for i in range(4):
        url = news_keyword_index[i]['url']
    for i in range(4):
        url_img = news_keyword_index[i]['urlToImage']

    return render_template("index.html", title=title, author=author, url=url, url_img=url_img, news_keyword_index=news_keyword_index, source=source)


@app.route('/top_ten_US_headlines', methods = ['GET', 'POST'])
def us_headlines():
    newsGenerator.news_info.get_news("us")
    access_title = main_functions.read_from_file("NEWS_FLASK/JSON_FILES/news_title.json")

    for i in range(9):
        access_range = access_title[i]['title']
    for i in range(9):
        access_author = access_title[i]['url']
    for i in range(9):
        access_source = access_title[i]['source']['name']
    for i in range(9):
        access_img = access_title[i]['urlToImage']
    return render_template("top_ten_us_headlines.html", access_range=access_range, access_title=access_title, access_author=access_author, access_img=access_img, access_source=access_source)


@app.route("/keyword_results/", methods = ['GET', 'POST'])
def keywords():
    keyword = request.form['keyword']
    print(keyword)

    url_keyword = keyword
    url = 'https://newsapi.org/v2/everything?q='
    url_api = '&apiKey=ba2f4cd4830c446daed332a6daa22afe'
    url3 = url + url_keyword + url_api
    response = requests.get(url3).json()

    main_functions.save_to_file(response, "NEWS_FLASK/JSON_FILES/news_keyword.json")
    keyword_index = main_functions.read_from_file("NEWS_FLASK/JSON_FILES/news_keyword.json")
    keyword_posts = keyword_index['articles']
    main_functions.save_to_file(keyword_posts, "NEWS_FLASK/JSON_FILES/keyword_result.json")
    news_keyword_index = main_functions.read_from_file("NEWS_FLASK/JSON_FILES/keyword_result.json")

    for i in range(4):
        title = news_keyword_index[i]['title']
    for i in range(4):
        author = news_keyword_index[i]['author']
    for i in range(4):
        url = news_keyword_index[i]['url']
    for i in range(4):
        url_img = news_keyword_index[i]['urlToImage']

    return render_template("keyword_results.html", keyword=keyword, title=title, author=author, url=url, url_img=url_img, news_keyword_index=news_keyword_index)


@app.route("/keyword_search", methods = ['GET', 'POST'])
def keyword_search():

    if request.method == 'POST':
        keyword=request.form['keyword']
        print(keyword)
        return redirect(url_for('keywords'))
    else:
        return render_template('keyword_search.html')


@app.route("/about", methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/country', methods=['GET','POST'])
def country():
    search_form = countryForm.country_info(request.form)
    if request.method == 'POST':
        country = request.form['country']
        country_info = newsGenerator.news_info.get_news(str(country))
        print(country[0])


        return render_template('country_results.html', form=search_form, country=country, country_info=country_info)
    return render_template("country_search.html", form=search_form)