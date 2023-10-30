import flet as ft 

def  main (page):

  # disabled property individuallly
  first_name = ft.TextField()
  last_name = ft.TextField()
  first_name.disabled = False
  last_name.disabled = False
  page.add(first_name, last_name)

  # disabled property by container group
  # first_name = ft.TextField()
  # last_name = ft.TextField()
  # c = ft.Column(controls=[
  #     first_name,
  #     last_name
  # ])
  # c.disabled = False
  # page.add(c)
  
ft.app(target=main, view=ft.AppView.WEB_BROWSER)