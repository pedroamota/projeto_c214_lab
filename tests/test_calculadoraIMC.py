import pytest
from .src.CalculadoraIMC import CalculadoraIMC, AlturaNegativa, PesoNegativo, IMCService

def test_calcularIMC():
    imc_service = IMCService()
    calculadora = CalculadoraIMC(imc_service)

    altura = 1.75
    peso = 70
    imc = calculadora.calcular_imc(altura, peso)
    
    assert imc == pytest.approx(22.86, 0.01)

def test_pesoNegativo():
    imc_service = IMCService()
    calculadora = CalculadoraIMC(imc_service)
    
    with pytest.raises(PesoNegativo):
        calculadora.calcular_imc(1.75, -70)

def test_alturaNegativa():
    imc_service = IMCService()
    calculadora = CalculadoraIMC(imc_service)
    
    with pytest.raises(AlturaNegativa):
        calculadora.calcular_imc(-1.75, 70)
