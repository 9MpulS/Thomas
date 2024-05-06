import flet as ft
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

    def theme_toggle(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            btn_theme.icon = ft.icons.LIGHT_MODE_OUTLINED
        else:
            page.theme_mode = "dark"
            btn_theme.icon = ft.icons.DARK_MODE
        page.update()

    flag = 0


    start_point = ft.TextField(label="Звідки", width=400, on_change=validate)
    end_point = ft.TextField(label="Куди", width=400, on_change=validate)

    strt_date = ft.TextField(label="Дата відправлення", width=200, hint_text="ДД/ММ/РРРР/Години")

    end_date = ft.TextField(label="Дата відправлення", width=200, hint_text="ДД/ММ/РРРР/Години")

    btn_srhc = ft.OutlinedButton(text="Пошук", width=200, disabled=True)
    btn_edit = ft.OutlinedButton(text="Редагувати", width=200, disabled=True)
    btn_theme = ft.IconButton(icon=ft.icons.DARK_MODE, on_click=theme_toggle)

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
                    strt_date,
                    end_date
                ], alignment=ft.MainAxisAlignment.CENTER
            ),

        ], alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(top_bar)
    page.add(panel_srch)

ft.app(target=main)
