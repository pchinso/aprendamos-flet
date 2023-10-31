import flet as ft

def main(page:ft.Page):

  page.title = 'Click to show text'


  def show_text_hover(e):

    # Events handler values 
    print('Control: ', e.control)
    print('Page: ', e.page)
    print('Target: ', e.target)
    print('Name: ', e.name)
    print('Data: ', e.data)

    if e.data == 'true':
      text.visible = True
      text.value = 'Your mouse is over button'
    else:
      text.visible = False

    page.update()

  def show_text_click(e):

    # Events handler values 
    print('Control: ', e.control)
    print('Page: ', e.page)
    print('Target: ', e.target)
    print('Name: ', e.name)
    print('Data: ', e.data)

    if e.name == 'click':
      text.visible = True
      text.value = 'You clicked button'
    else:
      text.visible = False

    page.update()    
  

  text = ft.Text(value='', visible=False)
  button = ft.ElevatedButton(text='Mouse Hover!', 
                             on_click=show_text_click, 
                             on_hover=show_text_hover)
  
  page.add(button,text)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)