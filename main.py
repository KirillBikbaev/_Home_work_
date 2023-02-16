from roman import *

Arabic_Numbers = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXIX']
print(Arabic_Numbers)
for i in Arabic_Numbers:
    print(i, '->' ,roman_to_int(i))

Numbers =[4, 58, 1994, 26, 99, 69, 80]
for i in Numbers:
    print(i, '->',int_to_roman(i))
