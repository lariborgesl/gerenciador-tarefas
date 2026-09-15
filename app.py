from tarefas import adicionar_tarefa, listar_tarefas


def executar():
    print("=== Gerenciador de Tarefas ===")

    tarefa = input("Digite uma nova tarefa: ")

    adicionar_tarefa(tarefa)

    print("\nTarefas cadastradas:")
    for item in listar_tarefas():
        print(f"- {item}")


if __name__ == "__main__":
    executar()
