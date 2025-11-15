# import requests

# BASE_URL = "http://localhost:5000/sentiment_analysis"


# def test_sentiment_positive():
#     payload = {"statement": "I love deep learning ❤️"}
#     response = requests.post(BASE_URL, json=payload)

#     # Check if request was successful
#     assert (
#         response.status_code == 200
#     ), f"API returned {response.status_code}: {response.text}"

#     # Extract response data
#     data = response.json()[0]
#     label = data.get("label")
#     score = data.get("score")

#     # Assertions for logic
#     assert label == "POSITIVE", f"Expected 'POSITIVE', got {label}"
#     assert score > 0.9, f"Expected score > 0.9, got {score}"
from app import app  # Import your Flask instance
import json


def test_sentiment_positive():
    client = app.test_client()

    payload = {"statement": "I love deep learning ❤️"}

    response = client.post(
        "/sentiment_analysis", data=json.dumps(payload), content_type="application/json"
    )

    # Check if request was successful
    assert (
        response.status_code == 200
    ), f"API returned {response.status_code}: {response.data}"

    # Extract response data
    data = response.get_json()[0]
    label = data.get("label")
    score = data.get("score")

    # Assertions for logic
    assert label == "POSITIVE", f"Expected 'POSITIVE', got {label}"
    assert score > 0.9, f"Expected score > 0.9, got {score}"
