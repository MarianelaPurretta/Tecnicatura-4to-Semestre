import math
from decimal import Decimal

# NaN (Not A Number)
a = float('nan')
print(f'a: {a}')

#Modulo math
a = float('nan')
print(f'Es de tipo NaN (Not A Number): {math.isnan(a)}')

#Modulo decimal
a = Decimal('nan')
print(f'Es de tipo NaN (Not A Number): {math.isnan(a)}')