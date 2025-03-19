import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

def get_questions():
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["results"]


question_data = get_questions()