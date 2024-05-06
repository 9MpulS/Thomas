import flet as ft
import mysql.connector
import datetime


def main(page: ft.Page):
    page.title = "Thomas"
    page.theme_mode = "dark"
    page.window_width = 1068
    page.window_height = 720
    page.window_resizable = False

    def validate(e):
        if all([start_point.value, end_point.value]):
            btn_srhc.disabled = False
            btn_edit.disabled = False
        else:
            btn_srhc.disabled = True
            btn_edit.disabled = True
        page.update()
    def pick(e):
        if all([date_picker.value, time_picker.value]):
            date_start.text = date_picker.value
    def theme_toggle(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            btn_theme.icon = ft.icons.LIGHT_MODE_OUTLINED
        else:
            page.theme_mode = "dark"
            btn_theme.icon = ft.icons.DARK_MODE
        page.update()

    time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
    )
    date_picker = ft.DatePicker(
        first_date=datetime.datetime(2024, 1, 1),
        last_date=datetime.datetime(2026, 1, 1),
    )

    start_point = ft.TextField(label="Звідки", width=400, on_change=validate)
    end_point = ft.TextField(label="Куди", width=400, on_change=validate)
    date_start = ft.CupertinoButton(text="Дата відправлення", width=200, on_click=lambda _: date_picker.pick_date())
    date_end = ft.CupertinoButton(text="Дата прибуття", width=200, on_click=lambda _: date_picker.pick_date())
    time_start = ft.CupertinoButton(text="Час відправлення", width=200, on_click=lambda _: time_picker.pick_time())
    time_end = ft.CupertinoButton(text="Час прибуття", width=200, on_click=lambda _: time_picker.pick_time())
    btn_srhc = ft.OutlinedButton(text="Пошук", width=200, disabled=True)
    btn_edit = ft.OutlinedButton(text="Редагувати", width=200, disabled=True)
    btn_theme = ft.IconButton(icon=ft.icons.DARK_MODE, on_click=theme_toggle)

    page.overlay.append(date_picker)
    page.overlay.append(time_picker)

    top_bar = ft.Row(
        [
            btn_theme,
        ], alignment=ft.MainAxisAlignment.END,
    )

    panel_srch = ft.Column(
        [
            ft.Row(
                [
                    start_point,
                    end_point,
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    date_start,
                    date_end
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    time_start,
                    time_end
                ], alignment=ft.MainAxisAlignment.CENTER
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )



    # def navigate(e):
    #     index = page.navigation_bar.selected_index
    #     page.clean()
    #     if index == 0:
    #         page.add(top_bar)
    #         page.add(panel_reg)
    #     elif index == 1:
    #         page.add(top_bar)
    #         page.add(panel_auth)

    # page.navigation_bar = ft.NavigationBar(
    #     destinations=[
    #         ft.NavigationDestination(icon=ft.icons.HOW_TO_REG_OUTLINED, label="Реєстрація"),
    #         ft.NavigationDestination(icon=ft.icons.HOW_TO_REG, label="Авторизація")
    #     ], on_change=navigate
    # )

    page.add(top_bar)
    page.add(panel_srch)


ft.app(target=main)
