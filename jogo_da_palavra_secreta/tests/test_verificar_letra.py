import pytest
from jogo_da_palavra_secreta.jogo_da_palavra_secreta import verificar_se_letra_esta_na_palavra

def test_verificar_true():
    assert verificar_se_letra_esta_na_palavra('a', 'amarelo') is True

def test_verificar_true2():
    assert verificar_se_letra_esta_na_palavra('A', 'amarelo') is True

def test_verificar_false():
    assert verificar_se_letra_esta_na_palavra('i', 'amarelo') is False

def test_tipo_invalido_letra():
    with pytest.raises(TypeError):
        verificar_se_letra_esta_na_palavra(2, 'computador')

def test_tipo_invalido_palavra():
    with pytest.raises(TypeError):
        verificar_se_letra_esta_na_palavra('o', ['computador'])

def test_valor_letra_vazia():
    with pytest.raises(ValueError):
        verificar_se_letra_esta_na_palavra('', 'python')

def test_valor_palavra_vazia():
    with pytest.raises(ValueError):
        verificar_se_letra_esta_na_palavra('y', '')

def test_valor_letra_mais_de_um_caractere():
    with pytest.raises(ValueError):
        verificar_se_letra_esta_na_palavra('ab', 'python')