import requests

result = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
result.raise_for_status()
questions = result.json()
question_data = questions["results"]
