import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("BMI Calculator")
app.geometry("300x350")
app.config(bg="#000")

font1 = ("Arial", 30, "bold")
font2 = ("Arial", 30, "bold")
font3 = ("Arial", 30, "bold")

title_label = customtkinter.CTkLabel(app, font=font1, text="BMI Calculator")
title_label.place(x=20, y=20)

app.mainloop()
