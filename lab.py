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

title_label = customtkinter.CTkLabel(
    app, font=font1, text="BMI Calculator", text_color="#fff", bg_color="#000"
)
title_label.place(x=20, y=20)

weight_label = customtkinter.CTkLabel(
    app, font=font2, text="Weight", text_color="#fff", bg_color="#000"
)
weight_label.place(x=20, y=80)

height_label = customtkinter.CTkLabel(
    app, font=font2, text="Height", text_color="#fff", bg_color="#000"
)
height_label.place(x=20, y=150)

weight_entry = customtkinter.CTkLabel(
    app, font=font2, text_color="#000", bg_color="#fff", border_color="#fff"
)
weight_entry.place(x=20, y=110)

height_entry = customtkinter.CTkLabel(
    app, font=font2, text_color="#000", bg_color="#fff", border_color="#fff"
)
weight_entry.place(x=20, y=180)

app.mainloop()
