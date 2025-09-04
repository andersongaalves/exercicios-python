import pytest
from calculadora_imc import calcular_imc

def test_imc_metros():
    assert calcular_imc(83.50, 1.82) == 25.21

def test_imc_centimetros():
    assert calcular_imc(80, 175) == 26.12

def test_tipo_invalido_peso():
    with pytest.raises(TypeError):
        calcular_imc('80', 175)

def test_tipo_invalido_altura():
    with pytest.raises(TypeError):
        calcular_imc(80, '175')

def test_valor_invalido_peso():
    with pytest.raises(ValueError):
        calcular_imc(0, 175)

def test_valor_invalido_altura():
    with pytest.raises(ValueError):
        calcular_imc(80, 0)