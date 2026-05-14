# Controle de temperaturas

# Criamos uma lista vazia para armazenar as temperaturas em Celsius
temperaturas_celsius = []

# Usamos um laço para ler as temperaturas até que o usuário digite "sair"
while True:
    temp = input("Digite uma temperatura em Celsius (ou 'sair' para encerrar): ")
    if temp.lower() == "sair":
        break
    try:
        temperaturas_celsius.append(float(temp))
    except ValueError:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")

# Criamos uma nova lista para armazenar as temperaturas convertidas em Fahrenheit
temperaturas_fahrenheit = [temp * 9/5 + 32 for temp in temperaturas_celsius]

# Calculamos as médias das temperaturas em Celsius e Fahrenheit
media_celsius = sum(temperaturas_celsius) / len(temperaturas_celsius) if temperaturas_celsius else 0
media_fahrenheit = sum(temperaturas_fahrenheit) / len(temperaturas_fahrenheit) if temperaturas_fahrenheit else 0

# Exibimos as médias na tela
print("-" * 20)
print(f"Média das temperaturas em Celsius: {media_celsius:.2f} °C")
print(f"Média das temperaturas em Fahrenheit: {media_fahrenheit:.2f} °F")
