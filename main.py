import random

import requests
import streamlit as st
i = 1
while i == 1:
    quote = []
    author = []
    optional = ["age", "alone", "amazing", "anger", "architecture", "art", "attitude", "beauty", "best", "birthday",
                "business", "car", "change", "communications", "computers", "cool", "courage", "dad", "dating", "death",
                "design", "dreams", "education", "environmental", "equality", "experience", "failure", "faith",
                "family",
                "famous", "fear", "fitness", "food", "forgiveness", "freedom", "friendship", "funny", "future", "god",
                "good", "government", "graduation", "great", "happiness", "health", "history", "home", "hope", "humor",
                "imagination", "inspirational", "intelligence", "jealousy", "knowledge", "leadership", "learning",
                "legal",
                "life", "love", "marriage", "medical", "men", "mom", "money", "morning", "movies", "success"]
    category = random.choice(optional)
    api_key = "fLbrL86fS63d/Dl15s1sng==Kooyhtryr2Y38nLU"
    url = f"https://api.api-ninjas.com/v1/quotes?category={category}"

    request = requests.get(url, headers={'X-Api-Key': api_key})
    content = request.json()

    # getting just quote from json
    for i in content:
        quote.append((i['quote']))
        author.append(i['author'])

    print(content)

    st.title("Random Quote")

    st.write(quote[0])
    st.write('-' + f'*{author[0]}*')
    i = 0

if st.button('Again'):
    i = 0
