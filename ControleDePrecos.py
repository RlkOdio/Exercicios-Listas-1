# Controle de preços

# Criamos uma lista vazia para armazenar os preços
precos = []

# Usamos um laço para repetir a leitura 5 vezes
for i in range(1, 6):
    preco = float(input(f"Digite o preço {i}: "))
    precos.append(preco)

# Exibimos o maior e o menor preço na tela
print("-" * 20)
print(f"Maior preço: {max(precos)}")
print(f"Menor preço: {min(precos)}")
