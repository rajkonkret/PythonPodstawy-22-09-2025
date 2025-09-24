import csv

filename = "records.csv"
filename = "records_dict.csv"
# filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))  # odczyt 1024 znakó
    print(dialect.delimiter)  # ;

    # ustaw ponownie odczyt na początek pliku
    csv_f.seek(0)

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x000001F502840580> iterator

    fields = next(csvreader)  # odczyt jedego wiersza, wskaźnik ustawiony na następny

    for row in csvreader:  # wystartuje od drugiego wiersza
        rows.append(row)

print('Fields:', fields)  # Fields: ['name', 'branch', 'year', 'cgpa']
print('Rows:', rows)  # Rows: [['radek', 'coe', '3', '0']]
# <_csv.reader object at 0x0000026248EC06A0>
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]
