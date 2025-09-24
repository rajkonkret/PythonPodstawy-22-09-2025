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
