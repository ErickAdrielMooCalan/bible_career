import tkinter as tk
import pygame
from PIL import Image, ImageTk  # Para trabajar mejor con imágenes grandes

class IntroScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Carrera Bíblica")
        self.master.geometry("1280x720")
        self.master.configure(bg="white")
        self.master.iconbitmap('assets/icons/main_icon.ico')
        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        # Crear un Frame que ocupe toda la ventana
        container = tk.Frame(self.master, bg="white")
        container.pack(expand=True)  # Expande para ocupar todo el espacio
        container.place(relx=0.5, rely=0.5, anchor="center")  # Lo centra

        pygame.mixer.music.load('assets/SFX/intro_sound.wav')  # Asegúrate de poner la ruta correcta
        pygame.mixer.music.play()

        # Cargar imagen del logo
        image_path = 'assets/images/adventist_logo.png'
        image = Image.open(image_path)
        image = image.resize((300, 300))
        self.logo = ImageTk.PhotoImage(image)

        # Mostrar la imagen
        self.label_logo = tk.Label(container, image=self.logo, bg="white")
        self.label_logo.pack(pady=(0, 10))  # Un pequeño espacio

        # Texto debajo del logo
        self.label_developer_1 = tk.Label(container, text="Iglesia Adventista de Opichén", font=("Arial", 19), bg="white")
        self.label_developer_2 = tk.Label(container, text="Desarrollado por Erick Moo", font=("Arial", 15), bg="white")
        self.label_developer_1.pack()
        self.label_developer_2.pack()

        # Después de 3 segundos, iniciar el menú principal
        self.master.after(3000, self.start_game)

    def start_game(self):
        # Detener el sonido después de 3 segundos
        pygame.mixer.music.stop()
        print("Aquí iríamos al menú principal... (todavía falta crearlo)")
        # Aquí después pondremos el cambio real de pantalla
