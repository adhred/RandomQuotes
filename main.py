import requests

# API CALL

api_key = "fLbrL86fS63d/Dl15s1sng==Kooyhtryr2Y38nLU"
url = "https://api.api-ninjas.com/v1/quotes?category=happiness"

request = requests.get(url, headers={'X-Api-Key': api_key})
content = request.json()

# getting just quote from json
for i in content:
    print(i['quote'])

