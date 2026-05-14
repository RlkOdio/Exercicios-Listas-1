#  Lista de tarefas

tarefas = [] 

# Usamos um laço para ler as tarefas até que o usuário digite "fim"
while True: 
    tarefa = input("Digite uma tarefa (ou 'fim' para encerrar): ")
    if tarefa.lower() == "fim":
        break
    tarefas.append(tarefa)

# Exibimos as tarefas na tela
print("-" * 20)
print("Tarefas cadastradas:")
for t in tarefas:
    print(t)
