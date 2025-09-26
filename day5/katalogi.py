import shutil
from pathlib import Path

base_path = Path("ops_example")
base_path2 = Path("ops_example/D")

print(base_path)
print(base_path2)  # ops_example\D
print(type(base_path))  # <class 'pathlib._local.WindowsPath'>

# jeśli katalog istnieje, zostanie usunięty
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

# tworzenie katalogu
base_path.mkdir()

path_b = base_path / 'A' / "B"
path_c = base_path / 'A' / "C"
path_d = base_path / 'A' / "D"

# FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\B'
# Brak katalogu A, powoduje, że nie można utworzyć w nim katalogu B
# path_b.mkdir()

# musimy jawnie powiedzieć, że ma stworzyć drzewo katalogów
path_b.mkdir(parents=True)

# katalog C stworzy, bo istnieje już A
path_c.mkdir()
