from flask import Flask

app = Flask(__name__)    #crete an instace of app

app.config['SECRET_KEY']='cop4814_news_project'  #key that we are going to use to collect cookies-data

from NEWS_FLASK import routes   #you need to import routes after you create the app