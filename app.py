# Imports
from transformers import pipeline
from flask import Flask, request

# app
app = Flask(__name__)
# load pipeline
sentiment_analysis_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)


# route
@app.route("/sentiment_analysis", methods=["POST"])
def sentiment_analysis():
    data = request.get_json()
    input_text = data.get("statement")
    output = sentiment_analysis_pipeline(input_text)

    return output


# main function to run
if __name__ == "__main__":
    app.run(host="localhost", port=5000)
