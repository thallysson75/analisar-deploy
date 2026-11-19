import pytest
from usuarios import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    excluir_usuario,
)


def test_cadastrar_usuario():
    usuarios = []
    usuario = cadastrar_usuario(usuarios, "Ana Silva", "ana@email.com")
    assert usuario["nome"] == "Ana Silva"
    assert len(usuarios) == 1


def test_nao_permitir_email_duplicado():
    usuarios = []
    cadastrar_usuario(usuarios, "Ana Silva", "ana@email.com")
    with pytest.raises(ValueError):
        cadastrar_usuario(usuarios, "Outra Ana", "ANA@email.com")


def test_validar_nome():
    with pytest.raises(ValueError):
        cadastrar_usuario([], "A", "ana@email.com")


def test_validar_email():
    with pytest.raises(ValueError):
        cadastrar_usuario([], "Ana Silva", "email-invalido")


def test_listar_usuarios():
    usuarios = []
    cadastrar_usuario(usuarios, "Ana Silva", "ana@email.com")
    assert len(listar_usuarios(usuarios)) == 1


def test_buscar_usuario():
    usuarios = []
    cadastrar_usuario(usuarios, "Ana Silva", "ana@email.com")
    assert buscar_usuario(usuarios, "ana silva")["email"] == "ana@email.com"


def test_usuario_nao_encontrado():
    assert buscar_usuario([], "Pessoa") is None


def test_excluir_usuario():
    usuarios = []
    cadastrar_usuario(usuarios, "Ana Silva", "ana@email.com")
    assert excluir_usuario(usuarios, "ana@email.com") is True
    assert usuarios == []


def test_excluir_usuario_inexistente():
    assert excluir_usuario([], "naoexiste@email.com") is False
