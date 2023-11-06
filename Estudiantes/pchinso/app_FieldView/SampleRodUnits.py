import flet as ft

class SampleRod(ft.BarChartRod):
    def __init__(self, y: float, hovered: bool = False):
        super().__init__()
        self.hovered = hovered
        self.y = y

    def _before_build_command(self):
        self.to_y = self.y + 1 if self.hovered else self.y
        self.color = ft.colors.YELLOW if self.hovered else ft.colors.WHITE
        self.border_side = (
            ft.BorderSide(width=1, color=ft.colors.GREEN_400)
            if self.hovered
            else ft.BorderSide(width=0, color=ft.colors.WHITE)
        )
        super()._before_build_command()

    def _build(self):
        self.tooltip = str(self.y)
        self.width = 22
        self.color = ft.colors.WHITE
        self.bg_to_y = 20
        self.bg_color = ft.colors.GREEN_300


def main(page: ft.Page):
    def on_chart_event(e: ft.BarChartEvent):
        for group_index, group in enumerate(chart.bar_groups):
            for rod_index, rod in enumerate(group.bar_rods):
                rod.hovered = e.group_index == group_index and e.rod_index == rod_index
        chart.update()

    def create_ring_container(chart):
      
      ring_container = ft.Container(
                                    chart, 
                                    bgcolor=ft.colors.GREEN_200, 
                                    padding=5, 
                                    border_radius=5, 
                                    expand=True,
                                    height=200
                                   )

      return ring_container
    
    bar_gr = []
    bottom_ax = []

    for g in range(18):
      bar_gr.append(ft.BarChartGroup(
                                     x=g,
                                     bar_rods=[SampleRod(g)],
                                    )
                    )
      bottom_ax.append(ft.ChartAxisLabel(value=g, label=ft.Text(g)))
    
    chart = ft.BarChart(
        bar_groups=bar_gr,
        bottom_axis=ft.ChartAxis(
                                labels=bottom_ax
                                ),
        on_chart_event=on_chart_event,
        interactive=True,
        )

    ring_group_container = []
    
    create_ring_container(chart=chart)
    
    page.add(create_ring_container(chart=chart))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)