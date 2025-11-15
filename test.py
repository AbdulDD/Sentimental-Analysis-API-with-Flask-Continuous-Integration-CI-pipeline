import requests

def test():
    url = "http://localhost:5000/"
    payload = {"statement": "I love deep learning ❤️"}
    
    response = requests.post(url, json=payload)
    
    # check if request was successful
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return

    data = response.json()
    data = data[0]
    label = data.get("label")
    score = data.get("score")
    
    print("Label:", label, "Score:", score)

    # Correct logical AND and score threshold
    if label == 'POSITIVE' and score > 0.9:
        return 'Test successful'
    else:
        return 'Test failed'

result = test()
print(result)
