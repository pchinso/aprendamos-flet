# User input

[Flet Doc: User Input](https://flet.dev/docs/guides/python/getting-user-input)

## Button

[Button events](./Leccion2-Button.py)

```python
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

```

## Counter

[Counter](./Leccion2-Counter.py)

```python
import flet as ft

def main(page:ft.Page):
  page.title = 'Flet Counter'
  page.vertical_alignment = ft.MainAxisAlignment.CENTER

  txt_num = ft.TextField(value='0', text_align='right', width=100)

  def minus_count(e):
    txt_num.value = str(int(txt_num.value) - 1)
    page.update()
  
  def add_count(e):
      txt_num.value = str(int(txt_num.value) + 1)
      page.update()
  
  page.add(
     ft.Row(
        [
          ft.IconButton(ft.icons.REMOVE, on_click=minus_count),
          txt_num,
          ft.IconButton(ft.icons.ADD, on_click=add_count)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
     )
  )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

## Textbox

[Textbox](./Leccion2-Textbox.py)

```python

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

```
