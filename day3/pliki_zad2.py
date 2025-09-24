import chardet

#  pip install chardet
with open('test.log', "r", encoding='utf-8') as f:
    raw_data = f.read()

print(raw_data)
# Parametr W
# Dopisane
# Dopisane
# Dopisane
# Dośpisane

# musimy wczytanie dane binarnie - wymaganie chardet
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'Parametr W\r\nDopisane\r\nDopisane\r\nDopisane\r\nDo\xc5\x9bpisane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6286286784188612, 'language': 'Turkish'}
# {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']

print("Kodowanie znaków:", encoding)
print(f"Trafność: {confidence * 100} %")
# Kodowanie znaków: utf-8
# Trafność: 87.625 %

print(raw_data.decode(encoding=encoding))
# Parametr W
# Dopisane
# Dopisane
# Dopisane
# Dośąźpisane
