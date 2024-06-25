import tkinter as tk
from tkinter import messagebox

from src.main.ServiceIMC import ServiceIMC
from src.main.CalculadoraIMC import CalculadoraIMC


class AlturaNegativa(Exception):
    pass

class PesoNegativo(Exception):
    pass

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        # Instancia o serviço e a calculadora
        self.imc_service = ServiceIMC()
        self.calculadora_imc = CalculadoraIMC(self.imc_service)

        # Criação dos widgets
        tk.Label(root, text="Altura (m):").pack()
        self.altura_entry = tk.Entry(root)
        self.altura_entry.pack()

        tk.Label(root, text="Peso (kg):").pack()
        self.peso_entry = tk.Entry(root)
        self.peso_entry.pack()

        self.result_label = tk.Label(root, text="", pady=10)
        self.result_label.pack()

        calculate_button = tk.Button(root, text="Calcular IMC", command=self.calcular_imc)
        calculate_button.pack()

    def calcular_imc(self):
        try:
            altura = float(self.altura_entry.get())
            peso = float(self.peso_entry.get())
            resultado = self.calculadora_imc.obter_resultado_imc(altura, peso)
            self.result_label.config(text=f"{resultado.mensagem} (IMC: {resultado.categoria})")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")
        except PesoNegativo as e:
            messagebox.showerror("Erro", str(e))
        except AlturaNegativa as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", "Um erro ocorreu durante o cálculo do IMC.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
