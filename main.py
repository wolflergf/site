from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def news():
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = "751aa5c95c6d4ffab434a38f93f35163"
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

