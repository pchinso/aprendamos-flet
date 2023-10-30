
import flet as ft

def main(page):
  
  page.add(ft.ElevatedButton(text= 'Click me!', 
                             on_click=button_clicked))
  
  def button_clicked(e):
    page.add(ft.Text('Clicked'))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
