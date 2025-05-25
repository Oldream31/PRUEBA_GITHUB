import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Modo oscuro
        self.modo_oscuro = False

        # Estilo
        self.estilo_claro = {"bg": "white", "fg": "black"}
        self.estilo_oscuro = {"bg": "#2e2e2e", "fg": "white"}

        # Campo de entrada
        self.entrada = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
        self.entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Botones
        botones = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for i, boton in enumerate(botones):
            tk.Button(
                root, text=boton, font=("Arial", 15), command=lambda b=boton: self.click_boton(b)
            ).grid(row=(i // 4) + 1, column=i % 4, sticky="nsew", padx=5, pady=5)

        # Botón de modo oscuro
        self.boton_modo = tk.Button(
            root, text="Modo Oscuro", font=("Arial", 12), command=self.toggle_modo
        )
        self.boton_modo.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Configurar filas y columnas
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        self.actualizar_tema()

    def click_boton(self, boton):
        if boton == "C":
            self.entrada.delete(0, tk.END)
        elif boton == "=":
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, str(resultado))
            except Exception:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "Error")
        else:
            self.entrada.insert(tk.END, boton)

    def toggle_modo(self):
        self.modo_oscuro = not self.modo_oscuro
        self.actualizar_tema()

    def actualizar_tema(self):
        estilo = self.estilo_oscuro if self.modo_oscuro else self.estilo_claro
        self.root.configure(bg=estilo["bg"])
        self.entrada.configure(bg=estilo["bg"], fg=estilo["fg"], insertbackground=estilo["fg"])
        self.boton_modo.configure(bg=estilo["bg"], fg=estilo["fg"], text="Modo Claro" if self.modo_oscuro else "Modo Oscuro")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()