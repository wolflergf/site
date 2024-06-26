from flask import Flask, render_template, request, redirect, url_for
from dotenv import dotenv_values
import requests
import openai
import json


config = dotenv_values(".env")
app = Flask(__name__)
API_KEY = config["KEY"]
openai.api_key = config["OPENAI_API_KEY"]


def get_colors(msg):
    # Define a prompt for generating color palettes based on text prompts
    prompt = f"""
    You are a color palette generating assistant. Your task is to create color palettes based on verbal descriptions, themes, moods, or instructions 				provided in the prompt. The color palettes should consist of 2 to 8 colors.

	**Example:**

	Q: Generate a color palette inspired by the following verbal description: "Sunset on the beach"
	A: ["#FF6B6B", "#FF8E1C", "#FFC300", "#FFE74C", "#5BC0EB", "#009BDD", "#021C1E"]

	**Desired Format:***
	
	The color palettes should be provided in a JSON array format, where each element is a hexadecimal color code.
	Q: Create a color palette based on the following verbal description: {msg}
	A:
    """
    # Send completion request to OpenAI API to generate color palette
    response = openai.Completion.create(
        prompt=prompt,
        model="davinci-002",
        max_tokens=200,
    )

    # Extract the generated colors from the API response
    colors = json.loads(response["choices"][0]["text"])
    return colors


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/news")
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


@app.route("/projects")
def projects_watermark():
    return render_template("watermark.html")


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}


@app.route("/palette_init")
def palette_init():
    return render_template("palette.html")


if __name__ == "__main__":
    app.run(debug=True)
