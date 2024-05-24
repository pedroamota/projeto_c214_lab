from src.main.ResultadoIMC import ResultadoIMC
class AlturaNegativa(Exception):
    pass

class PesoNegativo(Exception):
    pass

class IMCService:
    def classificar_imc(self, imc: float) -> ResultadoIMC:
        if imc < 16:
            return ResultadoIMC("Magreza grave", 3, "Seu IMC indica magreza grave, o que pode ser prejudicial à saúde.")
        elif 16 <= imc < 16.9:
            return ResultadoIMC("Magreza moderada", 2, "Seu IMC indica magreza moderada, o que pode ser um sinal de alerta.")
        elif 17 <= imc < 18.5:
            return ResultadoIMC("Magreza leve", 1, "Seu IMC indica magreza leve, que pode ser melhorado com uma dieta balanceada.")
        elif 18.6 <= imc < 24.9:
            return ResultadoIMC("Peso ideal", 0, "Parabéns! Seu IMC está dentro da faixa de peso ideal.")
        elif 25 <= imc < 29.9:
            return ResultadoIMC("Sobrepeso", 1, "Seu IMC indica sobrepeso. Considere adotar hábitos mais saudáveis.")
        elif 30 <= imc < 34.9:
            return ResultadoIMC("Obesidade grau I", 2, "Seu IMC indica obesidade grau I. É importante procurar orientação médica.")
        elif 35 <= imc < 39.9:
            return ResultadoIMC("Obesidade grau II", 3, "Seu IMC indica obesidade grau II. Procure ajuda médica para melhorar sua saúde.")
        else:
            return ResultadoIMC("Obesidade grau III", 4, "Seu IMC indica obesidade mórbida. É crucial buscar orientação médica imediata.")    
        
class Calculadora_IMC:
    def __init__(self, imc_service: IMCService):
        self.imc_service = imc_service

    def calcular_imc(self, altura: float, peso: float) -> float:
        if peso < 0:
            raise PesoNegativo("Peso negativo")

        if altura < 0:
            raise AlturaNegativa("Altura negativa")

        imc = peso / altura ** 2

        return imc 
    
    def obter_resultado_imc(self, altura: float, peso: float) -> ResultadoIMC:
        imc = self.calcular_imc(altura, peso)
        return self.imc_service.classificar_imc(imc)
    