tarefas = []

def separadores():
    print("-" * 100)
    print("=" * 100)
    print("-" * 100)

def mostrar_tarefas():
    if len(tarefas) > 0:
        for tarefa in enumerate(tarefas):
            print(f"    {tarefa[0] + 1}. {tarefa[1]}")
    else:
        print("A lista de tarefas esta vazia")

while True:
    separadores()
    print("Por favor, selecione uma das opções a seguir:")
    print("    1. Adicionar uma tarefa")
    print("    2. Remover uma tarefa")
    print("    3. Listar todas as tarefas")
    print("    4. Sair do programa")
    opcao = input("Insira sua opção: ")
    separadores()
    
    if opcao == "1":
        print("Adicionar Tarefa")
        tarefa_nome = input("Insira o nome da tarefa: ")
        tarefas.append(tarefa_nome)
        print(f"{tarefa_nome} foi adicionado(a) com sucesso")
    elif opcao == "2":
        mostrar_tarefas()
        tarefa_pos = int(input("Insira o número da tarefa: ")) - 1
        tarefa_nome = tarefas[tarefa_pos]
        tarefas.pop(tarefa_pos)
        print(f"{tarefa_nome} foi removido(a) com sucesso")
    elif opcao == "3":
        mostrar_tarefas()
    elif opcao == "4":
        print("Programa encerrando...")
        separadores()
        break