import tkinter as tk
import pygame
from PIL import Image, ImageTk


class MainMenuScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Carrera Bíblica - Menú Principal")
        self.master.geometry("1280x720")
        self.master.configure(bg="white")
        self.master.iconbitmap('assets/icons/main_icon.ico')
        pygame.mixer.init()

        # Cargar y redimensionar iconos
        self.icon_start = self.load_and_resize_icon('assets/icons/play_game.png')
        self.icon_questions = self.load_and_resize_icon('assets/icons/make_questions.png')
        self.icon_add_group = self.load_and_resize_icon('assets/icons/add_group.png')
        self.icon_about = self.load_and_resize_icon('assets/icons/about_us.png')
        self.icon_exit = self.load_and_resize_icon('assets/icons/exit_game.png')

        self.create_widgets()

    def load_and_resize_icon(self, file_path, size=(40, 40)):  # Ajusté el tamaño aquí
        image = Image.open(file_path)
        image = image.resize(size)  # Redimensionar la imagen
        return ImageTk.PhotoImage(image)  # Convertir a formato adecuado para Tkinter

    def create_widgets(self):
        # Contenedor para centrar todo
        container = tk.Frame(self.master, bg="white")
        container.pack(expand=True)

        # Música de fondo en loop
        pygame.mixer.music.load('assets/music/background_music_1.wav')
        pygame.mixer.music.play(loops=-1)

        # Título
        title_label = tk.Label(container, text="Carrera Bíblica", font=("Arial", 32), bg="white")
        title_label.pack(pady=30)

        # Botón 1: Iniciar carrera bíblica
        btn_start_career = tk.Button(
            container,
            text="Iniciar Carrera Bíblica",
            font=("Arial", 16),  # Ajusté el tamaño de la fuente
            width=300,  # Aumenté el tamaño del botón
            image=self.icon_start,
            compound="left",
            padx=15,  # Añadí espaciado entre el icono y el texto
            bg="#f0f0f0",  # Fondo claro para el botón
            command=self.start_career
        )
        btn_start_career.pack(pady=10)

        # Botón 2: Crear tus preguntas
        btn_create_questions = tk.Button(
            container,
            text="Crea tus preguntas",
            font=("Arial", 16),  # Ajusté el tamaño de la fuente
            width=300,  # Aumenté el tamaño del botón
            image=self.icon_questions,
            compound="left",
            padx=15,  # Añadí espaciado entre el icono y el texto
            bg="#f0f0f0",  # Fondo claro para el botón
            command=self.create_questions
        )
        btn_create_questions.pack(pady=10)

        # Botón 3: Agregar grupos
        btn_add_group = tk.Button(
            container,
            text="Agregar grupos",
            font=("Arial", 16),  # Ajusté el tamaño de la fuente
            width=300,  # Aumenté el tamaño del botón
            image=self.icon_add_group,
            compound="left",
            padx=15,  # Añadí espaciado entre el icono y el texto
            bg="#f0f0f0",  # Fondo claro para el botón
            command=self.add_groups
        )
        btn_add_group.pack(pady=10)

        # Botón 4: Acerca de nosotros
        btn_about_us = tk.Button(
            container,
            text="Acerca de nosotros",
            font=("Arial", 16),  # Ajusté el tamaño de la fuente
            width=300,  # Aumenté el tamaño del botón
            image=self.icon_about,
            compound="left",
            padx=15,  # Añadí espaciado entre el icono y el texto
            bg="#f0f0f0",  # Fondo claro para el botón
            command=self.about_us
        )
        btn_about_us.pack(pady=10)

        # Botón 5: Salir del programa
        btn_exit = tk.Button(
            container,
            text="Salir del programa",
            font=("Arial", 16),  # Ajusté el tamaño de la fuente
            width=300,  # Aumenté el tamaño del botón
            image=self.icon_exit,
            compound="left",
            padx=15,  # Añadí espaciado entre el icono y el texto
            bg="#f0f0f0",  # Fondo claro para el botón
            command=self.exit_program
        )
        btn_exit.pack(pady=10)

        # Añadir hover a cada botón
        buttons = [btn_start_career, btn_create_questions, btn_add_group, btn_about_us, btn_exit]
        for button in buttons:
            button.bind("<Enter>", self.on_enter)
            button.bind("<Leave>", self.on_leave)

    # Efecto al pasar el cursor
    def on_enter(self, event):
        event.widget.config(bg="#cce7ff")  # Azul clarito en hover

    def on_leave(self, event):
        event.widget.config(bg="#f0f0f0")  # Vuelve al color original

    # Funciones de los botones
    def start_career(self):
        print("Iniciaríamos la Carrera Bíblica aquí!")

    def create_questions(self):
        print("Aquí iríamos a la sección de crear preguntas.")

    def add_groups(self):
        print("Aquí agregaríamos nuevos grupos.")

    def about_us(self):
        print("Mostraríamos información acerca del proyecto.")

    def exit_program(self):
        print("Saliendo del programa...")
        self.master.quit()  # Cierra la aplicación

