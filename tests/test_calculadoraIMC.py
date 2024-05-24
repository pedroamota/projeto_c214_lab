import pytest

from src.main.CalculadoraIMC import AlturaNegativa, Calculadora_IMC, IMCService, PesoNegativo

def test_calcularIMC():
    imc_service = IMCService()
    calculadora = Calculadora_IMC(imc_service)

    altura = 1.75
    peso = 70
    imc = calculadora.calcular_imc(altura, peso)
    
    assert imc == pytest.approx(22.86, 0.01)

def test_pesoNegativo():
    imc_service = IMCService()
    calculadora = Calculadora_IMC(imc_service)
    
    with pytest.raises(PesoNegativo):
        calculadora.calcular_imc(1.75, -70)

def test_alturaNegativa():
    imc_service = IMCService()
    calculadora = Calculadora_IMC(imc_service)
    
    with pytest.raises(AlturaNegativa):
        calculadora.calcular_imc(-1.75, 70)
