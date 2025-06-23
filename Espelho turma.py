import random

nomes = [
    "ADRIAN", "ANGELO", "ARTHUR", "CARLOS", "CHRISTOPHER", "DOUGLAS",
    "EMANUELLY", "EVERSON", "GABRIEL", "GUILHERME", "GUSTAVO A", "GUSTAVO P",
    "GUSTAVO", "ISABELLA", "JAMILE", "JOAO M", "JOÃO O", "JOAQUIM",
    "KALIKEY", "LUIS", "MARIA", "PEDRO A", "PEDRO G", "RAFAEL", "RAPHAEL",
    "RAPHAEL", "ROBERTO", "SOFIA", "STEPHANIE"
]
nomes[27] = "SEU_NOME"

random.shuffle(nomes)

colunas = 4
largura = max(len(nome) for nome in nomes) + 2

while len(nomes) % colunas != 0:
    nomes.append("")

for i in range(0, len(nomes), colunas):
    linha = nomes[i:i+colunas]
    print("+" + "+".join("-" * largura for _ in linha) + "+")
    print("|" + "|".join(nome.center(largura) for nome in linha) + "|")
print("+" + "+".join("-" * largura for _ in linha) + "+")
