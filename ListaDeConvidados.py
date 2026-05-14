# Lista de convidados
convidados = [] 

# Usamos um laço para repetir a leitura 5 vezes
for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º convidado: ")
    convidados.append(nome)

# Exibimos os convidados na tela
print("-" * 20)
print("Convidados cadastrados:")
for c in convidados:
    print(c)

# Informamos quantos convidados foram cadastrados
print("-" * 20)
print(f"Total de convidados cadastrados: {len(convidados)}")
