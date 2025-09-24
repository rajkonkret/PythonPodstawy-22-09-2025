# działąnia z pliki
# filehandler - rura do pliku
# context manager
# with - context manager

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
# context manager zamyka plik za nas

# shift enter - plik w nowym oknie
with open('test.log', "w", encoding="utf-8") as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# "x" - gdy plik istnieje, doastajemy bład
# with open('test.log', "x", encoding="utf-8") as f:
#     f.write('PArametr X\n')

with open('test.log', "w", encoding="utf-8") as f:
    f.write('Parametr W\n')

with open('test.log', 'a', encoding="utf-8") as file:
    file.write("Dopisane\n")
    file.write("Dopisane\n")
    file.write("Dopisane\n")
    file.write("Dośpisane\n")

with open('test.log', "r", encoding="utf-8") as f:
    lines = f.read()

print(lines)
# Parametr W
# Dopisane
# Dopisane
# Dopisane
