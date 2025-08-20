#========================================================= Questão 1 ========================================================= 
tabuada = 9

with open("Tabuada_de_9.txt", 'w') as f:
    f.write("Tabuada do Número 9:\n")
    
    for count in range(1, 11):
        f.write(f"{tabuada} x {count} = {tabuada * count}\n")

    print("Arquivo criado com sucesso!")

#========================================================= Questão 2 ========================================================= 
nome = input("Digite seu nome: ")
rg = input("Digite seu RG: ")
cpf = input("Digite seu CPF: ")
try:
    ano_nasc = int(input("Digite seu ano de nascimento: "))
    ano_atual = 2025

    if ano_nasc == ano_atual:
        print("Erro: Tu nasceu ontem?")
    else:
        idade = ano_atual - ano_nasc

        with open("dados_pessoa.txt", 'w') as f:
            f.write("=== Dados da Pessoa ===\n")
            f.write(f"Nome: {nome}\n")
            f.write(f"RG: {rg}\n")
            f.write(f"CPF: {cpf}\n")
            f.write(f"Ano de Nascimento: {ano_nasc}\n")
            f.write(f"Idade: {idade} anos\n")

        print("Arquivo 'dados_pessoa.txt' criado!")

except ValueError:
    print("Erro: O ano de nascimento deve ser um número inteiro.")


#========================================================= Questão 3 ========================================================= 
arquivo = "dados_pessoa.txt"
linhas = []
with open(arquivo, 'r') as f:
    for linha in f:
        linhas.append(linha.strip())
print(linhas)

#========================================================= Questão 4 ========================================================= 
nome = input("Digite o nome do aluno: ")
try:
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))

    media = (nota1 + nota2) / 2

    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    with open("resultado_aluno.txt", "w") as f:
        f.write("Nome: " + nome + "\n")
        f.write("Média: " + str(media) + "\n")
        f.write("Situação: " + situacao + "\n")

    print("Dados salvos no arquivo 'resultado_aluno.txt' !")

except ValueError:
    print("Erro: Por favor, digite números para as notas.")

#========================================================= Questão 5 ========================================================= 
try:
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))

    soma = num1 + num2
    subt = num1 - num2
    mult = num1 * num2

    with open("resultados_calculadora.txt", "w") as f:
       f.write(f"Soma: {num1} + {num2} = {soma}\n")
        f.write(f"Subtração: {num1} - {num2} = {subt}\n")
        f.write(f"Multiplicação: {num1} * {num2} = {mult}\n")

       if num2 != 0:
            divisao = num1 / num2
            f.write(f"Divisão: {num1} / {num2} = {divisao}\n")
        else:
            f.write("Divisão: Erro! Divisão por zero não é permitida.\n")

    print("Resultados salvos no arquivo 'resultados_calculadora.txt'.")

except ValueError:
    print("Erro: Por favor, digite números inteiros válidos.")

#========================================================= Questão 6 ========================================================= 
try:
    nome = input("Digite seu nome: ")
    if not nome.strip():
        raise ValueError("Nome vazio não é válido.")
    if any(char.isdigit() for char in nome):
        raise ValueError("Nome não pode conter números.")
    print("Nome válido:", nome)
except ValueError as e:
    print("Erro:", e)

#========================================================= Questão 7 ========================================================= 
print("Digite dois números para divisão")

try:
    num1 = int(input("1º número : "))
    num2 = int(input("2º número: "))

    resultado = num1 / num2
    print("Resultado da divisão: ", resultado)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Você deve digitar apenas números inteiros.")

#========================================================= Questão 8 ========================================================= 
import math

entrada = input("Digite os números inteiros separados por espaço: ")

numeros = entrada.split()

for numero in numeros:
    try:
        numero = int(numero)
        if numero < 0:
            raise ValueError(f"{numero} não pode ser negativo.")
        fatorial = math.factorial(numero)
        print(f"O fatorial de {numero} é {fatorial}")  
    except ValueError as e:
        print("Erro:", e)

# ========================================================= Questão 9 ========================================================= 
import os

arquivo = "arquivo.txt"

if os.path.exists(arquivo):
    try:
        linhas = 0
        palavras = 0

        with open(arquivo, 'r') as f:
            for linha in f:
                linhas += 1
                palavras += len(linha.split())
        
        print(f"O arquivo '{arquivo}' tem {linhas} linhas e {palavras} palavras.")
    
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
else:
    print(f"O arquivo '{arquivo}' não existe no diretório.")

#========================================================= Questão 10 ========================================================= 
import os

def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    if not all(c.isalpha() or c.isspace() for c in nome):
        raise ValueError("Nome deve conter apenas letras e espaços.")
    return nome.title()

nome = input("Digite seu nome completo: ")

try:
    formatado = validar_nome(nome)
    arquivo = "nome_pessoa.txt"

    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            f.write(formatado)
        print(f"Nome '{formatado}' salvo no arquivo '{arquivo}'.")
    else:
        print(f"O arquivo '{arquivo}' já existe.")

except ValueError as e:
    print("Erro:", e)
except Exception as e:
    print("Erro inesperado:", e)

