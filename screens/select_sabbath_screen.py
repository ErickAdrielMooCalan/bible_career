import tkinter as tk
from tkinter import messagebox
from screens.main_menu_screen import MainMenuScreen  # Importamos la clase MainMenuScreen

class SelectSabbathScreen:
    def __init__(self, master):
        self.master = master  # Usamos la ventana principal directamente
        self.create_widgets()

    def create_widgets(self):
        # Limpiar todo el contenido de la ventana
        for widget in self.master.winfo_children():
            widget.destroy()

        # Aquí pondremos el frame donde irán los sábados
        saturdays_frame = tk.Frame(self.master)
        saturdays_frame.pack(fill=tk.BOTH, expand=True)

        # Botón para agregar un nuevo sábado
        new_saturday_button = tk.Button(
            saturdays_frame, text="Agregar Nuevo Sábado", command=self.add_saturday
        )
        new_saturday_button.pack(pady=10)

        # Botón para regresar al menú principal
        back_button = tk.Button(
            saturdays_frame, text="Regresar al Menú Principal", command=self.go_back_to_main_menu
        )
        back_button.pack(pady=10)

        # Cargar los sábados (más adelante de la base de datos)
        self.load_saturdays(saturdays_frame)

    def load_saturdays(self, saturdays_frame):
        # Por ahora datos simulados
        example_saturdays = ["Sábado 4 de mayo", "Sábado 11 de mayo", "Sábado 18 de mayo"]

        for saturday in example_saturdays:
            frame = tk.Frame(saturdays_frame)
            frame.pack(fill=tk.X, pady=5, padx=10)

            label = tk.Label(frame, text=saturday, anchor="w")
            label.pack(side=tk.LEFT, expand=True)

            button = tk.Button(frame, text="Ver preguntas", command=lambda s=saturday: self.open_questions(s))
            button.pack(side=tk.RIGHT)

    def add_saturday(self):
        messagebox.showinfo("Agregar Sábado", "Aquí podrás agregar un nuevo sábado.")

    def open_questions(self, saturday):
        messagebox.showinfo("Ver preguntas", f"Viendo preguntas para: {saturday}")

    def go_back_to_main_menu(self):
        # Primero destruye los widgets de la pantalla actual (SelectSabbathScreen)
        for widget in self.master.winfo_children():
            widget.destroy()

        # Luego carga el menú principal
        MainMenuScreen(self.master)  # Aquí volvemos a cargar la pantalla principal
