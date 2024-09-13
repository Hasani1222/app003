import flet as ft


def main(page: ft.Page):
        page.title="Suma de 2 numeros"
        page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        page.bgcolor="rojo"
    
        lbl1=ft.Text("Suma de 2 numeros",
                style=ft.TextStyle(size=40,weight="bold"))
    
        ing1=ft.Image(src="malilla.webp",width=200,height=200)
        
        btnnum1=ft.ElevatedButton("num1",
                            color="geen",
                            width=100,
                            height=50)
    
        btnnum2=ft.ElevatedButton("num2",
                            color="red",
                            width=100,
                            height=50)
        page.add(
        ft.Column(
            [
                lbl1,
                ing1,
                ft.Row([btnnum1,btnnum2],
                    alignment=ft.MainAxisAlignment.CENTER,
                    ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
        )
    )

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
ft.app(main)
