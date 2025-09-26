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
