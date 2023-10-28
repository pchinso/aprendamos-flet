# Instalacion y Hello World

## Windows Instalacion

Crear virtual enviroment e instalar Flet

Create a new virtual environment: 
Navigate to the directory where you want to create your project and run the following command:

```sh
pipenv shell
```

Install Flet:
With the virtual environment activated, you can now install your project dependencies using pip

```sh
pipenv install flet
```

Create hello-flet.py app
Basic flet app structure

```python
import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    pass

ft.app(target=main)

```

to run on webbrowser

```python
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

[Hello Flet app](./Leccion1-Hello-Flet-app.py)

```python
import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

```
