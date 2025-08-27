#Questão 1
try:
    with open("notas.txt", "r") as arquivo:
        palavras = arquivo.read()

except FileNotFoundError:
    with open("notas.txt", "w") as arquivo:
        arquivo.write("Arquivo criado.")
    with open("notas.txt", "r") as arquivo:
        palavras = arquivo.read()

print(palavras)

#Questão 2
try:
    with open("frases.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    linhas_nao_vazias = [linha for linha in linhas if linha.strip() != ""]
    print(f"Quantidade de linhas não vazias: {len(linhas_nao_vazias)}")

except FileNotFoundError:
    print("Ops! Você se esqueceu de criar o arquivo 'frases.txt' ")

except PermissionError:
    print("Ops! Parece que você não tem permissão para acessar esse arquivo!.")

#Questão 3
import re

try:
    with open("comentarios.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.read()

except FileNotFoundError:
    print("Ops! Você se esqueceu de criar o arquivo 'comentarios.txt' ")
    exit(1)

except UnicodeDecodeError:
    with open("comentarios.txt", "r", encoding="latin-1") as arquivo:
        palavras = arquivo.read()

limpeza = ' '.join(palavras.split())
limpeza = limpeza.replace("...", ".")

with open("comentarios_limpos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(limpeza)

print("Arquivo 'comentarios_limpos.txt' foi criado com sucesso.")


#Questão 4

jogadores_times = {}

try:
    with open("jogadores_times.txt", "r", encoding="utf-8") as arquivo:
        linhas_ruims = []
        for linha in arquivo:
            linha = linha.strip()

            try:
                nome, time = linha.split(",", 1)
                jogadores_times[nome.strip()] = time.strip()
            except ValueError:
                linhas_ruims.append(linha)
        
        try:
            with open("linhas_ruims.log", "w", encoding="utf-8") as log:
                for linha_ruim in linhas_ruims:
                    log.write(linha_ruim + "\n")
        except Exception as e:
            print(f"Erro ao escrever no log de linhas inválidas: {e}")
    
except FileNotFoundError:
    print("O arquivo 'jogadores_times.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")

print("Dicionário com jogadores e times:")
print(jogadores_times)

#Questão 5

try:
    with open("lista_a.txt", "r", encoding="utf-8") as arquivo_a:
        lista_a = set(arquivo_a.read().splitlines())
except FileNotFoundError:
    print("Arquivo 'lista_a.txt' não encontrado.")
    lista_a = set()

try:
    with open("lista_b.txt", "r", encoding="utf-8") as arquivo_b:
        lista_b = set(arquivo_b.read().splitlines())
except FileNotFoundError:
    print("Arquivo 'lista_b.txt' não encontrado.")
    lista_b = set()

lista_unica = sorted(lista_a.union(lista_b))

with open("lista_uniq.txt", "w", encoding="utf-8") as arquivo_saida:
    for item in lista_unica:
        arquivo_saida.write(item + "\n")

print("Arquivo 'lista_uniq.txt' foi criado com sucesso.")

#Questão 6
import string

try:
    with open("texto.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    texto_modificado = texto.lower()
    texto_modificado = texto_modificado.translate(str.maketrans("", "", string.punctuation))

    print("Conteúdo modificado do conjunto:")
    print(texto_modificado,"\n")

    palavras = texto_modificado.split()
    palavras_distintas = set(palavras)

    print("Palavras distintas no conjunto:")
    print(palavras_distintas)

    print(f"\nQuantidade de palavras distintas: {len(palavras_distintas)}")

except FileNotFoundError:
    print("Arquivo 'texto.txt' não encontrado.")

#Questão 7

try:
    with open("lista_a.txt", "r", encoding="utf-8") as arquivo_a:
        lista_a = arquivo_a.read().splitlines()
except FileNotFoundError:
    print("Arquivo 'lista_a.txt' não encontrado.")
    lista_a = []

try:
    with open("lista_b.txt", "r", encoding="utf-8") as arquivo_b:
        lista_b = arquivo_b.read().splitlines()
except FileNotFoundError:
    print("Arquivo 'lista_b.txt' não encontrado.")
    lista_b = []

lista_unica = sorted(set(lista_a + lista_b))

with open("lista_unica.txt", "w", encoding="utf-8") as arquivo_saida:
    for item in lista_unica:
        arquivo_saida.write(item + "\n")

print("Arquivo 'lista_unica.txt' foi criado com sucesso.")
