import flet as ft
import mysql.connector

def main(page: ft.Page):
    page.title = "Thomas"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False

    def register(e):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="@Vlad1234",
                database="thomas"
            )
            cursor = db.cursor()

            check_sql = """SELECT * FROM users WHERE login = %s"""
            check_val = (user_login.value,)
            cursor.execute(check_sql, check_val)
            if cursor.fetchone():
                page.snack_bar = ft.SnackBar(ft.Text("Користувач з таким логіном вже існує"))
                page.snack_bar.open = True
                page.update()
                db.close()
                return

            sql = """INSERT INTO users (login, passwd) VALUES (%s, %s)"""
            val = (user_login.value, user_passwd.value)
            cursor.execute(sql, val)
            db.commit()
            db.close()

            user_login.value = ""
            user_passwd.value = ""
            btn_reg.disabled = True
            page.update()

        except Exception as ex:
            print("Error:", ex)

    def validate(e):
        if all([user_login.value, user_passwd.value]):
            btn_reg.disabled = False
            btn_auth.disabled = False
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True
        page.update()

    def authorizate(e):
        admin_flag = False
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="@Vlad1234",
                database="thomas"
            )
            cursor = db.cursor()

            sql = """SELECT * FROM users WHERE login = %s AND passwd = %s"""
            val = (user_login.value, user_passwd.value)
            cursor.execute(sql, val)

            user_data = cursor.fetchone()

            if user_data:
                # user_login.value = ""
                # user_passwd.value = ""
                # btn_auth.text = "Авторизовано"
                # page.update()

                if user_data[3] == 1:
                    admin_flag = True
                else:
                    admin_flag = False
# Перехід на наступну сторінку з відровідними правами

            else:
                user_login.value = ""
                user_passwd.value = ""
                page.snack_bar = ft.SnackBar(ft.Text("Невірно введені пароль або логін"))
                page.snack_bar.open = True
                page.update()
            db.close()

        except Exception as ex:
            print("Error:", ex)

    def theme_toggle(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            btn_theme.icon = ft.icons.LIGHT_MODE_OUTLINED
        else:
            page.theme_mode = "dark"
            btn_theme.icon = ft.icons.DARK_MODE
        page.update()

    user_login = ft.TextField(label="Логін", width=200, on_change=validate)
    user_passwd = ft.TextField(label="Пароль", width=200, password=True, on_change=validate)
    btn_reg = ft.OutlinedButton(text="Зареєструватися", width=200, on_click=register, disabled=True)
    btn_auth = ft.OutlinedButton(text="Увійти", width=200, on_click=authorizate, disabled=True)
    btn_theme = ft.IconButton(icon=ft.icons.DARK_MODE, on_click=theme_toggle)

    top_bar = ft.Row(
        [
            btn_theme,
        ], alignment=ft.MainAxisAlignment.END
    )

    panel_reg = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Реєстрація"),
                    user_login,
                    user_passwd,
                    btn_reg
                ]
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    panel_auth = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Авторизація"),
                    user_login,
                    user_passwd,
                    btn_auth
                ]
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0:
            page.add(top_bar)
            page.add(panel_reg)
        elif index == 1:
            page.add(top_bar)
            page.add(panel_auth)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOW_TO_REG_OUTLINED, label="Реєстрація"),
            ft.NavigationDestination(icon=ft.icons.HOW_TO_REG, label="Авторизація")
        ], on_change=navigate
    )

    page.add(top_bar)
    page.add(panel_reg)


ft.app(target=main)
