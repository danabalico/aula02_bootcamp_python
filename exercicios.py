import math
######## Inteiros ('int')


#1. Escreva um programa que soma dois números inteiros inseridos 
# pelo usuário.

##num_01=int(input("Insira um numero inteiro: "))
##num_02=int(input("Insira outro numero inteiro: "))
##soma = num_01 + num_02
##print(soma)


#2.Crie um programa que receba um número do usuário e calcule o
# resto da divisão desse número por 5.

##num_01=int(input("Insira um numero inteiro: "))
##div = num_01 % 5
##print(div)

#3.Desenvolva um programa que multiplique dois números fornecidos 
# pelo usuário e mostre o resultado.

##num01 = int(input("Digite um valor: "))
##num02= int(input("Digite outro valor: "))
##multi = num01* num02
##print(multi)

#4.Faça um programa que peça dois 
# números inteiros e imprima a divisão inteira do primeiro pelo segundo.

##num_01=int(input("Insira um numero inteiro: "))
##num_02=int(input("Insira outro numero inteiro: "))
##div = num_01 // num_02
##print(div)

#5.Escreva um programa que calcule o quadrado de um número fornecido 
# pelo usuário.

##num01= int(input("Digite um numero: "))
##quadrado = num01**2
##print(quadrado)

#Escreva um Números de Ponto Flutuante (float)

#6.programa que receba dois números flutuantes e realize sua adição.

##num01 = float(input("Digite um numero: "))
##num02 = float(input("Digite outro número: "))
##soma = num01 + num02
##print(soma)


#7.Crie um programa que calcule a média de dois números flutuantes 
# fornecidos pelo usuário.

##num01 = float(input("Digite um numero: "))
##num02 = float(input("Digite outro número: "))
##media = (num01 + num02) / 2
##print(media)



#8.Desenvolva um programa que calcule a potência de um número 
# (base e expoente fornecidos pelo usuário).
#9.Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#10.Escreva um programa que calcule a área de um círculo, recebendo 
# o raio como entrada.

raio = float(input("Qual o raio do circulo? "))
area = float(math.pi * (raio**2))
print(f"{area:.2f}")



