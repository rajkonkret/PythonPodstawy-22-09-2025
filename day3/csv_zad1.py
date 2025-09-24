# csv - dane oddzielone znakiem podziału ,;tab
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv
from dataclasses import field

# csv - biblioteka do dziłąń z plikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', "3", 0]

dict_name = dict(zip(fields, row))
print(dict_name)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}
filename = 'records.csv'

# newline="" - ominięcie pustych linii
with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)  # zapis wiersza
    csvwriter.writerow(row)  # zapis wiersza

filename = "records_dict.csv"
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()  # nazwy kolumn
    csvwriter.writerow(dict_name)

products = [
    {"sku": 1, "exp_date": 'today', "price": 200},
    {"sku": 2, "exp_date": 'today', "price": 100},
    {"sku": 3, "exp_date": 'today', "price": 250},
    {"sku": 4, "exp_date": 'tomorrow', "price": 99},
    {"sku": 5, "exp_date": 'today', "price": 50.50},
    {"sku": 6, "exp_date": 'tomorrow', "price": 9.99},
]

print(products[0])  # {'sku': 1, 'exp_date': 'today', 'price': 200}
list_product = [key for key in products[0]]
print(list_product)  # ['sku', 'exp_date', 'price']

# delimiter=";" - wskazanie delimitera
filename = "records_discount.csv"
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=list_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)  # writerows - zapis listy słowników
