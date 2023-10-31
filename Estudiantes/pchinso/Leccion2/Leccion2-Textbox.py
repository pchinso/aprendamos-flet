import flet as ft

def main(page:ft.Page):
  def welcome(e):
    if not textbox.value:
      textbox.error_text = 'Insert your name'
    else:
      name = textbox.value
      page.clean()
      page.add(ft.Text(f'Hello, {name}. \nBe welcome!'))

  textbox = ft.TextField(
    label='Insert your Name', 
    width=100, 
    height=50
  )
  button = ft.ElevatedButton(text='Be Welcome', on_click=welcome)
  
  page.add(button, textbox)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)