nomes = []
print("Digite 10 nomes:")

contador = 0
while contador < 10:
    nome = input("Digite o nome {}: ".format(contador + 1))

    if not nome.replace(" ", "").isalpha():
        print("Nome inválido! Use apenas letras e espaços.")
        break 

    nomes.append(nome)
    contador += 1

if len(nomes) == 10:
    nomes.sort()
    
    print("\nQuantidade de letras (sem contar espaços):")
    for nome in nomes:
        letras = nome.replace(" ", "")
        print(nome, "tem", len(letras), "letras.")
