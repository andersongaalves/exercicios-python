import pytest
from lista_de_compras.lista_de_compras import inserir

#Testes saidas esperadas: str
def test_inserir_str():
    assert inserir('Pão', 2) == 'Pão 2x'

def test_inserir_qtd_float():
    assert inserir('Pão', 2.5) == 'Pão 2.5x'

def test_inserir_capitalizacao():
    assert inserir('cuscuz nordestino', 2) == 'Cuscuz Nordestino 2x'

#Testes saidas esperadas: list
def test_inserir_lista():
    assert inserir('Pão', 2, ['Manteiga 1x']) == ['Manteiga 1x', 'Pão 2x']

def test_inserir_lista_vazia():
    assert inserir('pão', 2, []) == ['Pão 2x']

#Testes TypeError
def test_inserir_name_tipo_invalido():
    with pytest.raises(TypeError):
        inserir(['Manteiga 1x', 'Pão 2x'], 1)

def test_inserir_qtd_tipo_invalido():
    with pytest.raises(TypeError):
        inserir('Manteiga', '1')

def test_inserir_list_tipo_invalido():
    with pytest.raises(TypeError):
        inserir('Pão', 2, ('Manteiga 2x', 'Café 1x'))

#Testes ValueError
def test_inserir_name_vazio():
    with pytest.raises(ValueError):
        inserir('', 2)

def test_inserir_qtd_vazio():
    with pytest.raises(ValueError):
        inserir('Manteiga', 0)