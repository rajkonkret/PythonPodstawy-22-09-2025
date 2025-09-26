# decimal - biblioteka do działania na precyzyjnych liczbach zmiennoprzecinkowych

from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')

print(kwota1 + kwota2)  # 15.75

# precyzja = Decimal('0.000')
precyzja = Decimal('0.00')

roznica = kwota1 - kwota2
print('Różnica:', roznica)  # Różnica: 4.75
print("Różnica (zaokrąglone):", roznica.quantize(precyzja))  # Różnica (zaokrąglone): 4.75

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)
print("Kwota z podatkiem (zaokrąglona):", kwota_z_podatkiem.quantize(precyzja))
# Kwota z podatkiem: 12.6075
# Kwota z podatkiem (zaokrąglona): 12.61
