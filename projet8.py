import requests
from bs4 import BeautifulSoup


url = 'https://fr.wikipedia.org/wiki/Informatique'

print("Obtenir et analyser le contenu HTML de la page")
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

print("Extraire le titre de l'article")
title = soup.title.string
print(f'Titre de l\'article : {title}')

print("Extraire le texte de l'article et mapper les titres à leurs paragraphes")




