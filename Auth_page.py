import flet as ft
import datetime
import mysql.connector


def main(page: ft.Page):
    page.title = "Thomas"
    page.theme_mode = "dark"
    page.window_width = 1068
    page.window_height = 720
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
                user_login.value = ""
                user_passwd.value = ""
                btn_auth.text = "Авторизовано"
                page.update()
                page.clean()
                if user_data[3] == 1:
                    admin_flag = True
                    page.add(panel_user)
                else:
                    admin_flag = False
                    page.add(panel_user)
                page.add(main_bar)
                page.update()
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
    user_passwd = ft.TextField(label="Пароль", width=200, password=True, can_reveal_password=True, on_change=validate)
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
                ], alignment=ft.MainAxisAlignment.CENTER
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


    date_text = ft.TextField(label="Дата відправлення", width=200, hint_text="YYYY/MM/DD")
    time_text = ft.TextField(label="Час відправлення", width=200, hint_text="hh:mm")

    def change_date(e):
        date_text.value = date_picker.value.strftime('%Y/%m/%d')
        page.update()

    def change_time(e):
        time_text.value = time_picker.value.strftime('%H:%M')
        page.update()

    date_picker = ft.DatePicker(
        on_change=change_date,
        first_date=datetime.datetime(2023, 1, 1),
        last_date=datetime.datetime(2026, 1, 1),
    )

    time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
        on_change=change_time,
    )

    page.overlay.append(date_picker)
    page.overlay.append(time_picker)

    start_point = ft.TextField(label="Звідки", width=400, on_change=validate)
    end_point = ft.TextField(label="Куди", width=400, on_change=validate)

    strt_date = ft.IconButton(icon=ft.icons.DATE_RANGE, on_click=lambda _: date_picker.pick_date())
    strt_time = ft.IconButton(icon=ft.icons.ACCESS_TIME, on_click=lambda _: time_picker.pick_time())

    btn_srhc = ft.OutlinedButton(text="Пошук", width=200, disabled=True)
    btn_edit = ft.OutlinedButton(text="Редагувати", width=200, disabled=True)
    btn_theme = ft.IconButton(icon=ft.icons.DARK_MODE, on_click=theme_toggle)


    panel_user = ft.Column(
        [
            ft.Row(
                [
                    start_point,
                    end_point,
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    strt_date,
                    date_text,
                    time_text,
                    strt_time
                ], alignment=ft.MainAxisAlignment.CENTER
            ),

        ], alignment=ft.MainAxisAlignment.CENTER
    )

    def navigate_outh(e):
        index = auth_bar.selected_index
        page.clean()
        if index == 0:
            page.add(top_bar)
            page.add(panel_reg)
            page.add(auth_bar)
        elif index == 1:
            page.add(top_bar)
            page.add(panel_auth)
            page.add(auth_bar)

    def navigate_main(e):
        index = main_bar.selected_index
        page.clean()
        if index == 0:
            page.add(top_bar)
            page.add(panel_user)
            page.add(main_bar)
        elif index == 1:
            pass
        elif index == 2:
            page.add(top_bar)
            page.add(panel_auth)
            page.add(auth_bar)

    auth_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOW_TO_REG_OUTLINED, label="Реєстрація"),
            ft.NavigationDestination(icon=ft.icons.HOW_TO_REG, label="Авторизація")
        ], on_change=navigate_outh
    )

    main_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Пошук квитків"),
            ft.NavigationDestination(icon=ft.icons.FILE_DOWNLOAD_OUTLINED, label="Зберегти інформацію"),
            ft.NavigationDestination(icon=ft.icons.EXIT_TO_APP, label="Вихід")
        ], on_change=navigate_main
    )


    page.add(top_bar)
    page.add(panel_reg)
    page.add(auth_bar)



ft.app(target=main)
