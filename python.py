from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Correct initialization
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]

    response = client.responses.create(
        model="gpt-4o-mini",
        input=user_text
    )

    reply = response.output_text
    return reply

if __name__ == "__main__":
    app.run(debug=True)  
