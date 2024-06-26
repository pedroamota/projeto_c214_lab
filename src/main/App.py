import tkinter as tk
from tkinter import messagebox

from src.main.CalculadoraIMC import AlturaNegativa, PesoNegativo, IMCService, Calculadora_IMC


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.geometry("400x300")

        # Instancia o serviço e a calculadora
        self.imc_service = IMCService()
        self.calculadora_imc = Calculadora_IMC(self.imc_service)

        # Criação dos frames para centralizar os widgets
        altura_frame = tk.Frame(root)
        altura_frame.pack(pady=(60, 10))

        peso_frame = tk.Frame(root)
        peso_frame.pack(pady=10)

        # Criação dos widgets dentro dos frames
        tk.Label(altura_frame, text="Altura (m):").pack(side="left")
        self.altura_entry = tk.Entry(altura_frame)
        self.altura_entry.pack(side="left")

        tk.Label(peso_frame, text="Peso (kg):").pack(side="left")
        self.peso_entry = tk.Entry(peso_frame)
        self.peso_entry.pack(side="left")

        self.result_label = tk.Label(root, text="", pady=10)
        self.result_label.pack()

        calculate_button = tk.Button(root, text="Calcular IMC", command=self.calcular_imc)
        calculate_button.pack(pady=10)

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
