# REST API (Reprezentational State Transfer Application Programming Interface) to interfejs programowania aplikacji,
# który przestrzega zasad stylu architektonicznego REST,
# umożliwiając aplikacjom komunikację i wymianę danych.
# Korzysta ze standardowych protokołów HTTP (takich jak GET, POST, PUT, DELETE)
# Metody HTTP: Do operacji na zasobach wykorzystuje się standardowe metody HTTP:
# GET: Pobranie zasobu.
# POST: Utworzenie nowego zasobu.
# PUT: Zaktualizowanie istniejącego zasobu.
# DELETE: Usunięcie zasobu
# https://api.chucknorris.io/
import requests

#  pip install requests
url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)  # <Response [200]>

# 2xx - ok
# 3xx - warningi, przekierwoania
# 4xx - 404 - brak strony, 400 bad Request - błedne wywołnie
# 5xx - błędy po stronie serwera, 500 Internal Server Error

print(response.text)
