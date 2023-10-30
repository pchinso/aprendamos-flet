
import flet as ft

def main(page):
  def button_clicked(e):
    page.add(ft.Text('Clicked'))

  page.add(ft.ElevatedButton(text= 'Click me!', 
                             on_click=button_clicked))
  
ft.app(target=main, view=ft.AppView.WEB_BROWSER)