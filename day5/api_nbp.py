# url = "https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/"
import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"

response = requests.get(url)
print(response)  # <Response [200]>
print(response.text)

data = response.json()
print(data)
# {'table': 'A',
# 'currency': 'dolar amerykański',
# 'code': 'USD',
# 'rates': [{'no': '187/A/NBP/2025', 'effectiveDate': '2025-09-26', 'mid': 3.6528}]}

print(data['rates'])  # [    {'no': '187/A/NBP/2025', 'effectiveDate': '2025-09-26', 'mid': 3.6528}    ]
print(data['rates'][0])  # {'no': '187/A/NBP/2025', 'effectiveDate': '2025-09-26', 'mid': 3.6528}
print(data['rates'][0]['mid'])
