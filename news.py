from flask import Flask, render_template, url_for
import requests

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "751aa5c95c6d4ffab434a38f93f35163"
newscatcher = "o96VTWqkD__2SO4bnM0aCsybtoz1NSxYCzRALp4wUOY"
KEY_WORD = "Python, -swallows, -swallowed"
newscatcher_endpoint = "https://api.newscatcherapi.com/v2/search"


newscatcher_params = {
    "x-api-key": newscatcher,
    "q": KEY_WORD,
}
news_params = {
        "apiKey": NEWS_API_KEY,
        "q": KEY_WORD,
    }

news_response = requests.get(newscatcher_endpoint, params=newscatcher_params)
articles = news_response.json()["articles"]
three_articles = articles[:4]

print(three_articles)