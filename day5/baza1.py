# baza danych - system przechowywania danych
# silnik - mechanizm zarządzania danymi w bazie danych
# sql, nosql
# sqlite, mysql, postgress, oracle, mssql
import sqlite3  # korzysta z bazy sqlite

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baaza danych zostałą podłączona")
except sqlite3.Error as e:
    print("Bład połaczenia z bazą:", e)
finally:
    if conn:
        conn.close()
        print('Połączenie zostało zamknięte')
