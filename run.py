import flet as ft
import mysql.connector
from docx import Document

# Підключення до бази даних MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="@Vlad1234",
        database="Test"
    )
    cursor = db.cursor()

except:
    pass


def main(page: ft.Page):
    page.title = "Tomas"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False

    def register(e):
        pass

    def validate(e):
        if all([user_login.value, user_passwd.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True
        page.update()

    user_login = ft.TextField(label="Логін", width=200, on_change=validate)
    user_passwd = ft.TextField(label="Пароль", width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text="Зареєструватися", width=200, on_click=register, disabled=True)

    page.add(
        ft.Row(
        [
                ft.Column(
                    [
                        ft.Text("Реєстрація"),
                        user_login,
                        user_passwd,
                        btn_reg
                    ]
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main)
