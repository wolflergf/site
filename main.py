from flask import Flask, render_template, request, redirect, url_for
from dotenv import dotenv_values
import requests


config = dotenv_values(".env")
app = Flask(__name__)
API_KEY = config["KEY"]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def news():
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = API_KEY
    KEY_WORD = "Python, -swallows, -swallowed"
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": KEY_WORD,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:4]
    return render_template("news.html", all_articles=three_articles)


@app.route('/projects')
def projects_watermark():
    return render_template('watermark.html')


if __name__ == '__main__':
    app.run(debug=True)
