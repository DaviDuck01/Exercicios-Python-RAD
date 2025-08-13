#Questão 1
dna = input("Insira a cadeira de Dna que queria reverter: ").upper()
dna = "".join(reversed(dna))
print(dna)

#Questão 2
with open("texto.txt", "r") as arquivo:
    palavras = arquivo.read()
print("Este arquivo tem:", len(palavras.split), "palavras")

#Questão 3
with open("texto.txt", "r") as arquivo:
    palavras = arquivo.read()
palavras = palavras.replace(" ", "_")
print(palavras)

#Questão 4
with open("texto.txt", "r") as arquivo:
    palavras = arquivo.read()
palavras = list(dict.fromkeys(palavras.split()))
print(palavras)
