from tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    remover_tarefa,
    limpar_tarefas
)


def test_adicionar_tarefa():
    limpar_tarefas()
    adicionar_tarefa("Estudar Python")

    assert "Estudar Python" in listar_tarefas()


def test_concluir_tarefa():
    limpar_tarefas()
    adicionar_tarefa("Fazer atividade")

    resultado = concluir_tarefa(0)

    assert resultado is True
    assert "CONCLUÍDA" in listar_tarefas()[0]


def test_remover_tarefa():
    limpar_tarefas()
    adicionar_tarefa("Tarefa teste")

    resultado = remover_tarefa(0)

    assert resultado is True
    assert len(listar_tarefas()) == 0
