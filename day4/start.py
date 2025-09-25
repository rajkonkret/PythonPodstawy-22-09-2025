# import fun8
#
# fun8.all_params(1, 2, 3, 4)
# # a=1, b=2
# # c=3, d=4

import pakiet

# AttributeError: module 'pakiet' has no attribute 'powitanie'
# po dodaniu w __init__.py metoda jest widoczna
pakiet.powitanie()
# pakiet.info() # brak w __init__.py

# można plik z pakietu zaimportować bezpośrednio
from pakiet import fun

fun.powitanie()
fun.info()

# import jako alias
import pakiet.fun as pk

pk.powitanie()
pk.info()
