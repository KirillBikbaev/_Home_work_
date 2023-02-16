from roman import *

Arabic_Numbers = [str(i) for i in input('Римское число для преобразования в арабское: ').split()]
print(Arabic_Numbers)
for i in Arabic_Numbers:
    print(i, '->' ,roman_to_int(i))

Numbers = [int(i) for i in input('Арабское число для преобразования в римское: ').split()]
#[4, 58, 1994, 26, 99, 69, 80]
for i in Numbers:
    print(i, '->',int_to_roman(i))
