### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
CONSTANTE_BONUS= 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome:  ")

# PROBLEMAS QUE PODEM ACONTECER

## digitou um numero no lugar do nome
if nome_usuario.isdigit(): # isdigit() é para ver se tem um digito
    print("Você digitou seu nome errado.")
    exit() # para abortar o processo

## nao digitou nada
elif len(nome_usuario)== 0:
    print("Voce nao digitou nada")
    exit() # para abortar o processo

## digitou só espaço
elif nome_usuario.isspace():
    print("Você digitou só espaço")
    exit()


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario_usuario = input("Digite o valor do seu salário: ")

## PROBLEMAS QUE PODEM ACONTECER

# digitar letras
if salario_usuario.isalpha():
    print("Você não deve digitar letras")
    exit()

# não digitou nada
elif len(salario_usuario) == 0:
    print("Você não digitou nada")
    exit()

# digitar espaço
elif salario_usuario.isspace():
    print("Você digitou apenas espaços")
    exit()

try:
    #transformando em float para conseguir comparar com 0
    salario_usuario = float(salario_usuario)

    # digitou um salário igual a 0
    if salario_usuario == 0:
        print("O seu salário deve ser maior que zero para o calculo fazer sentido")
        exit()

    # digitou um salário negativo
    elif salario_usuario < 0:
        print("O seu salário deve ser positivo para fazer sentido")
        exit()
except ValueError:
    print("Você digitou um valor inválido. Por favor, insira um número.")



# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus: "))

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, 
# salário e bônus

print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?