
import flet as ft
import time

PATH_LIST = list() 

def write_list_values_as_txt(my_list=list()):
  # Open the file in "write" mode
  with open('output.txt', 'w') as file:
    # Iterate over each item in the list
    for item in my_list:
      # Write each item to a new line in the text file
      file.write(item + '\n')


def main(page: ft.Page):

  def step1(e):

    PATH_LIST.append(set_path_text_field.value)
    set_path_text_field.value = 'path/to/path2'
    next_button.on_click = step2

    page.update()

  def step2(e):
    
    PATH_LIST.append(set_path_text_field.value)
    set_path_text_field.value = 'path/to/path3'
    next_button.on_click = step3

    page.update()

 
  def step3(e):
    
    PATH_LIST.append(set_path_text_field.value)
    set_path_text_field.value = 'path/to/path4'

    page.update()
    page.clean()
    page.add(ft.Text('Final values to output.txt',size=22))
    for val in  PATH_LIST:
      page.add(ft.Text(val))
    write_list_values_as_txt(PATH_LIST)



  # Page design
  page.padding = 30
  page.spacing = 30

  # Page elements

  set_path_text_field = ft.TextField(value='path/to/path1') 
  next_button = ft.ElevatedButton(text= 'Next!', 
                                  on_click=step1) 
  
  
  page.add(set_path_text_field, next_button)

  
if __name__ == '__main__':

  ft.app(target=main, view=ft.AppView.WEB_BROWSER)