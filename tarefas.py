tarefas = []


def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)


def listar_tarefas():
    return tarefas


def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice] = tarefas[indice] + " - CONCLUÍDA"
        return True
    return False


def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        return True
    return False


def limpar_tarefas():
    tarefas.clear()


def buscar_tarefa(palavra):
    return [
        tarefa for tarefa in tarefas
        if palavra.lower() in tarefa.lower()
    ]
