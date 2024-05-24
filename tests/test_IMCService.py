import pytest

from src.main.CalculadoraIMC import IMCService

#criando uma instancia de IMCService para os testes
@pytest.fixture
def imc_service():
    return IMCService()

def test_magreza_grave(imc_service):
    resultado = imc_service.classificar_imc(15.0)
    assert resultado.estado == "Magreza grave"
    assert resultado.criticidade == 3
    assert resultado.comentario == "Seu IMC indica magreza grave, o que pode ser prejudicial à saúde."

def test_magreza_moderada(imc_service):
    resultado = imc_service.classificar_imc(16.5)
    assert resultado.estado == "Magreza moderada"
    assert resultado.criticidade == 2
    assert resultado.comentario == "Seu IMC indica magreza moderada, o que pode ser um sinal de alerta."

def test_magreza_leve(imc_service):
    resultado = imc_service.classificar_imc(17.5)
    assert resultado.estado == "Magreza leve"
    assert resultado.criticidade == 1
    assert resultado.comentario == "Seu IMC indica magreza leve, que pode ser melhorado com uma dieta balanceada."

def test_peso_ideal(imc_service):
    resultado = imc_service.classificar_imc(22.0)
    assert resultado.estado == "Peso ideal"
    assert resultado.criticidade == 0
    assert resultado.comentario == "Parabéns! Seu IMC está dentro da faixa de peso ideal."

def test_sobrepeso(imc_service):
    resultado = imc_service.classificar_imc(27.0)
    assert resultado.estado == "Sobrepeso"
    assert resultado.criticidade == 1
    assert resultado.comentario == "Seu IMC indica sobrepeso. Considere adotar hábitos mais saudáveis."

def test_obesidade_grau_I(imc_service):
    resultado = imc_service.classificar_imc(32.0)
    assert resultado.estado == "Obesidade grau I"
    assert resultado.criticidade == 2
    assert resultado.comentario == "Seu IMC indica obesidade grau I. É importante procurar orientação médica."

def test_obesidade_grau_II(imc_service):
    resultado = imc_service.classificar_imc(37.0)
    assert resultado.estado == "Obesidade grau II"
    assert resultado.criticidade == 3
    assert resultado.comentario == "Seu IMC indica obesidade grau II. Procure ajuda médica para melhorar sua saúde."

def test_obesidade_grau_III(imc_service):
    resultado = imc_service.classificar_imc(42.0)
    assert resultado.estado == "Obesidade grau III"
    assert resultado.criticidade == 4
    assert resultado.comentario == "Seu IMC indica obesidade mórbida. É crucial buscar orientação médica imediata."
