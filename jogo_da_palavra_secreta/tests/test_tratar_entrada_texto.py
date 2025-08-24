import pytest
from jogo_da_palavra_secreta.jogo_da_palavra_secreta import tratar_input_texto

def test_tratar_texto_return():
    assert tratar_input_texto(' não vou SAir') == 'não vou sair'

def test_tratar_texto_entrada_tipo_invalido():
    with pytest.raises(TypeError):
        tratar_input_texto(3)

def test_tratar_texto_entrada_vazia():
    with pytest.raises(ValueError):
        tratar_input_texto('')