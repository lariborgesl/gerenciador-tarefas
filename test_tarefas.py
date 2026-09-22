from tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    remover_tarefa,
    limpar_tarefas,
    buscar_tarefa
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


def test_listar_tarefas():
    limpar_tarefas()
    adicionar_tarefa("Tarefa 1")
    adicionar_tarefa("Tarefa 2")

    tarefas = listar_tarefas()

    assert len(tarefas) == 2
    assert "Tarefa 1" in tarefas
    assert "Tarefa 2" in tarefas


def test_buscar_tarefa():
    limpar_tarefas()
    adicionar_tarefa("Estudar Python")
    adicionar_tarefa("Fazer atividade")

    resultado = buscar_tarefa("Python")

    assert len(resultado) == 1
    assert "Estudar Python" in resultado


def test_indice_invalido():
    limpar_tarefas()

    assert concluir_tarefa(0) is False
    assert remover_tarefa(0) is False
