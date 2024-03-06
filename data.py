import requests
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
questions = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean", params=parameters)
questions.raise_for_status()
data = questions.json()
question_data = data["results"]
