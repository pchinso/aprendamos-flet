import flet as ft

name = "Card example"

def create_card(
      icon=ft.Icon(ft.icons.ALBUM),
      title=ft.Text("Title"), 
      subtitle= ft.Text("Subtitle"),
      buttons=[ft.TextButton("Button1"), 
               ft.TextButton("Button2")],
      alignment= ft.MainAxisAlignment.END,
      width = 300,
      padding = 5):
    
    w = width
    p = padding

    return ft.Card(
            content=ft.Container(
             content=ft.Column(
             [
             ft.ListTile(
                 leading=icon,
                 title=title,
                 subtitle=subtitle
             ),
             ft.Row(
                 buttons,
                 alignment=alignment,
             ),
             ]
             ),
             width=w,
             padding=p,
            )
        )

def main(page:ft.Page):
    
    card1 = []
    card2 = []
    page.window_full_screen = False


    w = 260
    p = 5
    
    for n_ring in [51,50,31,30,11,10]:
      card1.append(create_card(
          icon=ft.Icon(ft.icons.ADD_CHART_ROUNDED),
          title=ft.Text("Ring"), 
          subtitle= ft.Text(str(n_ring)),
          buttons=[ft.TextButton("View"), 
                  ft.TextButton("Update"),
                  ft.TextButton("Select Date")],
          alignment= ft.MainAxisAlignment.END,
          width=w,
          padding=p
      )
      )

    for n_ring in [53,52,33,32,13,12]:
      card2.append(create_card(
          icon=ft.Icon(ft.icons.ADD_CHART_ROUNDED),
          title=ft.Text("Ring"), 
          subtitle= ft.Text(str(n_ring)),
          buttons=[ft.TextButton("View"), 
                  ft.TextButton("Update"),
                  ft.TextButton("Select Date")],
          alignment= ft.MainAxisAlignment.END,
          width=w,
          padding=p
      )
      )       
    for c in range(0,len(card1)):
       
    #   page.add(ft.Row(controls=[card1[c]],alignment=ft.MainAxisAlignment.START))
    #   page.add(ft.Row(controls=[card2[c]], alignment=ft.MainAxisAlignment.SPACE_EVENLY))      

    # for c in range(0,len(card1)):

    #   page.add(ft.Row(controls=[card2[c]], alignment=ft.MainAxisAlignment.SPACE_EVENLY))      
      page.add(ft.Row(
                  [
                      ft.Container(ft.Row(controls=[card1[c]]),
                          bgcolor=ft.colors.ORANGE_300,
                          alignment=ft.alignment.center,
                          expand=1,
                      ),
                      ft.VerticalDivider(),
                      ft.Container(ft.Row(controls=[card2[c]]),
                          bgcolor=ft.colors.BROWN_400,
                          alignment=ft.alignment.center,
                          expand=1,
                      ),
                      ft.VerticalDivider(),
                      ft.Container(
                          bgcolor=ft.colors.BLUE_300,
                          alignment=ft.alignment.center,
                          expand=1,
                      ),
                      ft.VerticalDivider(),
                      ft.Container(
                          bgcolor=ft.colors.GREEN_300,
                          alignment=ft.alignment.center,
                          expand=1,
                      ),
                  ],
                  spacing=0,
                  width=(w*4)+(p*4)+(10*8),
                  height=150, 
                  auto_scroll=True,
      )
      )

ft.app(target=main)