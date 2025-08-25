import pytest
from jogo_da_palavra_secreta.jogo_da_palavra_secreta import adicionar_letra_correta

#Testes saídas esperadas
def test_adicionar_letra_correta():
    assert adicionar_letra_correta('a', 'amarelo', '*******') == 'a*a****'

def test_adicionar_letra_correta_upper():
    assert adicionar_letra_correta('A', 'amarelo', '*******') == 'a*a****'

def test_adicionar_letra_correta_espaço():
    assert adicionar_letra_correta(' A ', 'amarelo', '*******') == 'a*a****'

def test_adicionar_letra_incorreta():
    assert adicionar_letra_correta('y', 'amarelo', '*******') == '*******'

#Testes TypeError
def test_adicionar_letra_tipo_incorreto():
    with pytest.raises(TypeError):
        adicionar_letra_correta(['a'], 'amarelo', '*******')

def test_adicionar_palavra_tipo_incorreto():
    with pytest.raises(TypeError):
        adicionar_letra_correta('a', ('amarelo', 'python'), '*******')

def test_adicionar_palavra_final_tipo_incorreto():
    with pytest.raises(TypeError):
        adicionar_letra_correta('a', 'amarelo', 7)

#Testes ValueError
def test_adicionar_letra_numero():
    with pytest.raises(ValueError):
        adicionar_letra_correta('2', 'amarelo', '*******')

def test_adicionar_letra_vazia():
    with pytest.raises(ValueError):
        adicionar_letra_correta('', 'amarelo', '*******')

def test_adicionar_palavra_vazia():
    with pytest.raises(ValueError):
        adicionar_letra_correta('a', '', '*******')

def test_adicionar_palavra_final_vazia():
    with pytest.raises(ValueError):
        adicionar_letra_correta('a', 'amarelo', '')