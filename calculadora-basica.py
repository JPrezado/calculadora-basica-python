print("Olá! Bem-vindo à calculadora.")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = int(input("Digite o número da operação desejada: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
elif operacao == 4:
    if num2 != 0:  #condicional para evitar divisão por zero
     resultado = num1 / num2
    else:
     resultado = "ERRO! Divisão por zero!"

else:
    resultado = "ERRO! Operação inválida!"

print ("O resultado é: ", resultado)

    
