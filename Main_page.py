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
                    date_text,
                    strt_time,
                    time_text
                ], alignment=ft.MainAxisAlignment.CENTER
            ),

        ], alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(top_bar)
    page.add(panel_srch)

ft.app(target=main)
