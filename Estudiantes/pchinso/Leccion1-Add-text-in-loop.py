import flet as ft
import time


def main(page):
  t = ft.Text()
  page.add(t)

  for i in range(10):
    t.value = f'Step {i}'
    page.update()
    time.sleep(1)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)