
import flet as ft
import json
import os

USER = dict() 

USER = {
  'user_name' : '',
  'user_surname' : '',
  'user_mail' : '',
  'user_phone' : '',
}

def write_dict_values_as_json(my_dict=dict()):

  file_path = 'output.json'
  try:
    # Check if the file exists
    if os.path.exists(file_path):
      # Read existing data from the JSON file
      with open(file_path, 'r') as file:
        existing_data = json.load(file)

        # Append the new dictionary to the existing data
        existing_data.append(my_dict)
    else:
        # If the file doesn't exist, create a new one with the given dictionary
        existing_data = [my_dict]

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("Data saved successfully.")

  except Exception as e:
    print(f"An error occurred: {e}")

def main(page: ft.Page):

  def step1(e):
    
    USER['user_name'] = name_field.value
    USER['user_surname'] = surname_field.value
    USER['user_mail'] = mail_field.value
    USER['user_phone'] = phone_field.value

    page.update()
    page.clean()
    page.add(ft.Text('Final values to output.txt',size=22))
    for val in  USER.values():
      page.add(ft.Text(val))

    write_dict_values_as_json(USER)



  # Page design
  page.padding = 30
  page.spacing = 30

  # Page elements

  name_field = ft.TextField(hint_text='Name')
  surname_field = ft.TextField(hint_text='SurName')
  mail_field = ft.TextField(hint_text='mail@mail.com')
  phone_field = ft.TextField(hint_text='666-666-666')

  next_button = ft.ElevatedButton(text= 'Next!', 
                                  on_click=step1) 
  
  
  page.add(name_field,
           surname_field,
           mail_field,
           phone_field,
           next_button)

  
if __name__ == '__main__':

  ft.app(target=main, view=ft.AppView.WEB_BROWSER)