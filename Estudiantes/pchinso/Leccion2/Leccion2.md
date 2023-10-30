# User input

[Flet Doc: User Input](https://flet.dev/docs/guides/python/getting-user-input)

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
