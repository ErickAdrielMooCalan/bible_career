import tkinter
import sqlite3

import tkinter as tk
from screens.intro_screen import IntroScreen

def main():
    root = tk.Tk()
    app = IntroScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
