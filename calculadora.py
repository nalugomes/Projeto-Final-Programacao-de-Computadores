
import re

operação = input('Qual a operação? ')
conta = re.search(r'^(\d)+(\+|\-|\*|\/)+(\d)$', operação)

a = int(conta.group(1))
b = str(conta.group(2))
c = int(conta.group(3))

if b == '+':
   resultado = a + c

elif b == '-':
   resultado = a - c

elif b == '*':
   resultado = a * c
else:
   resultado = a / c

print(resultado)
