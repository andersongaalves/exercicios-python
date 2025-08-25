import pytest
from jogo_da_palavra_secreta.jogo_da_palavra_secreta import mensagem_erros_de_entrada_de_texto

#Testes retornos esperados: str
def test_erros_de_limite():
    assert mensagem_erros_de_entrada_de_texto('ab', 1) == 'Por favor, digite apenas 1 letra'

def test_erros_de_limite_maior_que_1():
    assert mensagem_erros_de_entrada_de_texto('abc', 2) == 'Por favor, digite apenas 2 letras'

def test_erros_entrada_numero_sem_nome_campo():
    assert mensagem_erros_de_entrada_de_texto('7', 1) == 'Por favor, não digite números'

def test_erros_entrada_numero():
    assert mensagem_erros_de_entrada_de_texto('7', 1, 'Letra') == 'Letra não pode ser um número'

#Testes retornos esperados: bool
def test_erros_nenhum_erro():
    assert mensagem_erros_de_entrada_de_texto('a', 1, 'Letra') is False

#Testes TypeError
def test_erros_entrada_tipo_invalido():
    with pytest.raises(TypeError):
        mensagem_erros_de_entrada_de_texto(12)

def test_erros_limite_letras_tipo_invalido():
    with pytest.raises(TypeError):
        mensagem_erros_de_entrada_de_texto('a', '1')

def test_erros_nome_campo_tipo_invalido():
    with pytest.raises(TypeError):
        mensagem_erros_de_entrada_de_texto('a', 1, ['Letra', 'a'])

#Testes ValueError
def test_erros_entrada_vazia():
    with pytest.raises(ValueError):
        mensagem_erros_de_entrada_de_texto('')