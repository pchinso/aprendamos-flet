import flet as ft

def main(page):
  page.add(
    ft.Row(controls=[
      ft.Text('Text 1'),
      ft.Text('Text 2'),
      ft.Text('Text 3'),
    ])
  )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)