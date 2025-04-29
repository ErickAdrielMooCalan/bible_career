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

        # Cargar y redimensionar iconos normales y hover
        self.icon_start = self.load_and_resize_icon('assets/icons/main_menu_icons/play_game.png')
        self.icon_start_hover = self.load_and_resize_icon('assets/icons/main_menu_icons/play_game_hover.png')  # Icono hover
        self.icon_questions = self.load_and_resize_icon('assets/icons/main_menu_icons/make_questions.png')
        self.icon_questions_hover = self.load_and_resize_icon('assets/icons/main_menu_icons/make_questions_hover.png')  # Icono hover
        self.icon_add_group = self.load_and_resize_icon('assets/icons/main_menu_icons/add_group.png')
        self.icon_add_group_hover = self.load_and_resize_icon('assets/icons/main_menu_icons/add_group_hover.png')  # Icono hover
        self.icon_about = self.load_and_resize_icon('assets/icons/main_menu_icons/about_us.png')
        self.icon_about_hover = self.load_and_resize_icon('assets/icons/main_menu_icons/about_us_hover.png')  # Icono hover
        self.icon_exit = self.load_and_resize_icon('assets/icons/main_menu_icons/exit_game.png')
        self.icon_exit_hover = self.load_and_resize_icon('assets/icons/main_menu_icons/exit_game_hover.png')  # Icono hover

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

       # Frame de los logos principales
        logos_frame = tk.Frame(container, bg="white")
        logos_frame.pack(fill="x", padx=30, pady=10)  # Usar todo el ancho

        # Configurar las columnas para separación
        logos_frame.columnconfigure(0, weight=1)  # Columna izquierda
        logos_frame.columnconfigure(1, weight=8)  # Columna vacía más ancha para separar aún más
        logos_frame.columnconfigure(2, weight=1)  # Columna derecha

        # Cargar imágenes
        adventist_image = Image.open('assets/images/adventist_logo.png')
        adventist_image = adventist_image.resize((100, 100))
        adventist_photo = ImageTk.PhotoImage(adventist_image)

        ja_image = Image.open('assets/images/ja_logo.png')
        ja_image = ja_image.resize((100, 100))
        ja_photo = ImageTk.PhotoImage(ja_image)

        # Logo Adventista (izquierda)
        adventist_label = tk.Label(logos_frame, image=adventist_photo, bg="white")
        adventist_label.image = adventist_photo
        adventist_label.grid(row=0, column=0, sticky="w", padx=80)  # Aumenté más el padx aquí

        # Columna vacía (espacio)
        empty_label = tk.Label(logos_frame, bg="white")  # Columna vacía para separación
        empty_label.grid(row=0, column=1, sticky="w", padx=400)  # Aquí puedes ajustar el espacio vacío

        # Logo JA (derecha)
        ja_label = tk.Label(logos_frame, image=ja_photo, bg="white")
        ja_label.image = ja_photo
        ja_label.grid(row=0, column=2, sticky="e", padx=80)  # Aumenté más el padx aquí también

        # Título con imagen
        title_frame = tk.Frame(container, bg="white")
        title_frame.pack(pady=30)

        # Cargar imagen del título
        title_image = Image.open('assets/images/bible_race.png')  # Aquí pones tu imagen
        title_image = title_image.resize((100, 100))  # Ajusta el tamaño si es necesario
        title_photo = ImageTk.PhotoImage(title_image)

        # Etiqueta de la imagen
        title_image_label = tk.Label(title_frame, image=title_photo, bg="white")
        title_image_label.image = title_photo  # ¡Importante! Para que no se borre la imagen
        title_image_label.pack(side="left", padx=(0, 10))  # Separación entre imagen y texto

        # Etiqueta del texto
        title_label = tk.Label(title_frame, text="Carrera Bíblica", font=("Arial", 32), bg="white")
        title_label.pack(side="left")

        # Botones
        self.buttons = []

        # Botón 1: Iniciar carrera bíblica
        btn_start_career = self.create_button(container, "Iniciar Carrera Bíblica", self.icon_start, self.icon_start_hover, self.start_career)
        btn_start_career.pack(pady=10)

        # Botón 2: Crear tus preguntas
        btn_create_questions = self.create_button(container, "Crea tus preguntas", self.icon_questions, self.icon_questions_hover, self.create_questions)
        btn_create_questions.pack(pady=10)

        # Botón 3: Agregar grupos
        btn_add_group = self.create_button(container, "Agregar grupos", self.icon_add_group, self.icon_add_group_hover, self.add_groups)
        btn_add_group.pack(pady=10)

        # Botón 4: Acerca de nosotros
        btn_about_us = self.create_button(container, "Acerca de nosotros", self.icon_about, self.icon_about_hover, self.about_us)
        btn_about_us.pack(pady=10)

        # Botón 5: Salir del programa
        btn_exit = self.create_button(container, "Salir del programa", self.icon_exit, self.icon_exit_hover, self.exit_program)
        btn_exit.pack(pady=10)

    def create_button(self, container, text, normal_icon, hover_icon, command):
        button = tk.Button(
            container,
            text=text,
            font=("Arial", 16),
            width=300,
            image=normal_icon,
            compound="left",
            padx=15,
            bg="#f0f0f0",
            command=command
        )
        button.normal_icon = normal_icon
        button.hover_icon = hover_icon
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        self.buttons.append(button)  # Añadir botón a la lista
        return button

    # Efecto al pasar el cursor
    def on_enter(self, event):
        event.widget.config(bg="#cce7ff")
        button = event.widget
        button.config(image=button.hover_icon)

    def on_leave(self, event):
        event.widget.config(bg="#f0f0f0")
        button = event.widget
        button.config(image=button.normal_icon)

    # Funciones de los botones
    def start_career(self):
        print("Iniciaríamos la Carrera Bíblica aquí!")

    def create_questions(self):
        # Primero elimina todo lo anterior (destruye los widgets del intro)
        for widget in self.master.winfo_children():
            widget.destroy()

        # Luego crea un nuevo frame o pantalla dentro de la misma ventana
        from screens.select_sabbath_screen import SelectSabbathScreen

        # Esto crea el frame de la nueva pantalla en lugar de abrir una ventana nueva.
        new_screen = SelectSabbathScreen(self.master)

    def add_groups(self):
        print("Aquí agregaríamos nuevos grupos.")

    def about_us(self):
        print("Mostraríamos información acerca del proyecto.")

    def exit_program(self):
        print("Saliendo del programa...")
        self.master.quit()  # Cierra la aplicación
