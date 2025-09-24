from datetime import date, datetime, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-09-24
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print('Aktualna godzina:', time)  # Aktualna godzina: 2025-09-24 13:36:05.345565
print(type(time))  # <class 'datetime.datetime'>

print(today.year)
print(today.day)
# 2025
# 24

print(time.hour)
print(time.minute)
# 13
# 37

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data:", formated_date)  # Sformatowana data: 24/09/2025

# 13:39
formated_time = datetime.now().strftime("%H:%M:%S")
print("Sforamtowana godzina:", formated_time)  # Sforamtowana godzina: 13:42:52

# 12h
formated_time_12h = datetime.now().strftime("%I:%M:%S %p")
print("Sforamtowana godzina (12h):", formated_time_12h)  # Sforamtowana godzina (12h): 01:46:47 PM

# tomorrow = today + 1# TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie:", tomorrow)  # Jutro będzie: 2025-09-25

products = [
    {"sku": 1, "exp_date": today, "price": 200},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": today, "price": 250},
    {"sku": 4, "exp_date": tomorrow, "price": 99},
    {"sku": 5, "exp_date": today, "price": 50.50},
    {"sku": 6, "exp_date": tomorrow, "price": 9.99},
]

for p in products:
    # print(p)  # {'sku': 1, 'exp_date': datetime.date(2025, 9, 24), 'price': 200}
    # print(p['exp_date'])  # 2025-09-24

    if p['exp_date'] != today:
        continue  # wróć na początek pętli, nie rób kolejnych instrukcji

    p['price'] *= 0.8  # zmiana ceny, p = p * 0.8
    print(f"""Price for sku {p['sku']}
is now {p['price']}
""")
# Price for sku 1
# is now 160.0
#
# Price for sku 2
# is now 80.0
#
# Price for sku 3
# is now 200.0
#
# Price for sku 5
# is now 40.400000000000006
