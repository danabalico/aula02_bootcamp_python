# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, 
# utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     temp= float(input("Digite a temperatura em Celcius: "))
#     conversao = (temp * 1.8) + 32
#     print(f"{temp}°C é igual a {conversao}°F" )
# except ValueError:
#     print("Por favor, digite um número válido para a temperatura")






# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e 
# pontuações). Utilize try-except para garantir que a 
# entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.


# frase= input("Digite uma palavra ou frase: ")
# if isinstance(frase, str) and frase.replace(" ", "").isalpha():
#     frase_formatada = frase.replace(" ", "").lower()
#     if frase_formatada == frase_formatada[:: -1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palvra ou frase")





# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas 
# e um operador (+, -, *, /) do usuário. Use try-except para lidar com
# divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação 
# matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

# try:
#     num01=float (input("Digite um número: "))
#     num02= float(input("Digite outro número: "))
#     operador= input("Digite o operador desejado (+, -, *, /): ")

#     if operador == '+':
#         resultado = num01 + num02
#     elif  operador == '-' :
#         resultado = num01 - num02
#     elif operador == '*':
#         resultado = num01 * num02
#     elif operador == '/' and num02 != 0:
#         resultado = num01 / num02
#     else:
#         print("Resultado inválido ou divisão por zero")
#     print("Resultado:", resultado)

# except ValueError:
#      print("Erro: Entrada inválida. Certifique-se de inserir números.")

     



# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize 
# if-elif-else para classificar o número como "positivo", 
# "negativo" ou "zero". Adicionalmente, identifique se o número 
# é "par" ou "ímpar".

# try:
#     num01=float(input("Digite um número: "))

#     if num01 > 0:
#         print("O número digitado é positivo")
#     elif num01 == 0:
#         print("O número digitado é zero")
#     else:
#         print("O número digitado é negativo")

#     if num01 % 2 == 0:
#         print("O número digitado é par")
#     else:
#         print("O número digitado é ímpar")

# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números 
# separados por vírgula. O programa deve converter a string de 
# entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número 
# e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um 
# elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, 
# imprima a lista de inteiros.

lista_entrada= input("Digite uma lista de numeros, separados por vírgula")
numeros_str = lista_entrada.split(",") #split separa
numeros_int = [] # estou criando uma lista vazia
try:
    for num in numeros_str:
        numeros_int.append(num.strip())#strip remove espaços em branco
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: Certifique-se que todos os elementos são números inteiros válidos")