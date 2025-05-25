import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        self.root.resizable(True, True)

        # Modo oscuro
        self.modo_oscuro = False

        # Estilo
        self.estilo_claro = {"bg": "#ffefd5", "fg": "#000000"}  # Fondo amarillo claro
        self.estilo_oscuro = {"bg": "#2e2e2e", "fg": "#ffffff"}  # Fondo oscuro

        # Campo de entrada
        self.entrada = tk.Entry(root, font=("Arial", 24), justify="right", bd=10)
        self.entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Botones
        self.botones = []  # Lista para almacenar los botones
        botones = [
            ("7", "numero"), ("8", "numero"), ("9", "numero"), ("/", "operacion"),
            ("4", "numero"), ("5", "numero"), ("6", "numero"), ("*", "operacion"),
            ("1", "numero"), ("2", "numero"), ("3", "numero"), ("-", "operacion"),
            ("C", "especial"), ("0", "numero"), ("=", "especial"), ("+", "operacion")
        ]

        for i, (texto, tipo) in enumerate(botones):
            if tipo == "numero":
                color = "#ffb6c1"  # Rosa claro
            elif tipo == "operacion":
                color = "#87ceeb"  # Azul claro
            else:  # especial
                color = "#ffa07a"  # Naranja claro

            boton = tk.Button(
                root, text=texto, font=("Arial", 18), bg=color, fg=self.estilo_claro["fg"],
                command=lambda b=texto: self.click_boton(b)
            )
            boton.grid(row=(i // 4) + 1, column=i % 4, sticky="nsew", padx=5, pady=5)
            self.botones.append(boton)  # Guardar el botón en la lista

        # Botón de modo oscuro
        self.boton_modo = tk.Button(
            root, text="Modo Oscuro", font=("Arial", 14), command=self.toggle_modo
        )
        self.boton_modo.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Configurar filas y columnas para que se expandan
        for i in range(6):  # 5 filas de botones + 1 fila de entrada
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 columnas
            root.grid_columnconfigure(i, weight=1)

        # Vincular el evento de redimensionamiento
        self.root.bind("<Configure>", self.ajustar_fuente)

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

        # Actualizar colores de los botones
        for boton in self.botones:
            boton.configure(fg=estilo["fg"])

    def ajustar_fuente(self, event):
        # Calcular el tamaño de la fuente basado en el ancho de la ventana
        nuevo_tamano = max(12, int(self.root.winfo_width() / 25))
        self.entrada.configure(font=("Arial", nuevo_tamano))
        for boton in self.botones:
            boton.configure(font=("Arial", nuevo_tamano))
        self.boton_modo.configure(font=("Arial", max(10, nuevo_tamano - 4)))

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()