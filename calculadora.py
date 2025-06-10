import re

operação = input("Digite uma operação simples (ex: 12+5): ").replace(" ", "")

# Expressão regular para encontrar dois números inteiros com um operador entre eles
padrao = r'^(\d+)([+\-*/])(\d+)$'
conta = re.fullmatch(padrao, operação)

if conta:
    a = int(conta.group(1))
    operador = conta.group(2)
    b = int(conta.group(3))

    if operador == '+':
        resultado = a + b
    elif operador == '-':
        resultado = a - b
    elif operador == '*':
        resultado = a * b
    elif operador == '/':
        if b != 0:
            resultado = a / b
        else:
            resultado = "Erro: divisão por zero!"
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida. Use o formato: número operador número (ex: 10+5)")


