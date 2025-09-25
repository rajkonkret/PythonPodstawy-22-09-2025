import pandas

#  pip install pandas

data = pandas.read_csv('records_dict.csv')
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3     0

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)  # [['radek' 'coe' 3 0]]

data = pandas.read_csv("records_discount.csv", delimiter=";")
print(data)
#    sku  exp_date   price
# 0    1     today  200.00
# 1    2     today  100.00
# 2    3     today  250.00
# 3    4  tomorrow   99.00
# 4    5     today   50.50
# 5    6  tomorrow    9.99
