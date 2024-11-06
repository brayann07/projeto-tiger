import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog

# Conexão com o banco de dados
hotelbanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hoteltiger"
)
cursor = hotelbanco.cursor()

# Interface Gráfica
janela = tk.Tk()
janela.title("Hotel Tiger")
janela.geometry("800x400")
janela.configure(background='#FFDAB9')

janela.mainloop()
