class AlturaNegativa(Exception):
    pass

class PesoNegativo(Exception):
    pass

class IMCService:
    pass

class CalculadoraIMC:
    def __init__(self, imc_service: IMCService):
        self.imc_service = imc_service

    def calcular_imc(self, altura: float, peso: float) -> float:
        if peso < 0:
            raise PesoNegativo("Peso negativo")

        if altura < 0:
            raise AlturaNegativa("Altura negativa")

        imc = peso / altura ** 2

        return imc 