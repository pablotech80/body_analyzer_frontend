import reflex as rx
from state.my_state import (
    MyState,
)  # Asegúrate de tener el estado de la aplicación configurado


def index():
    return rx.Container(
        rx.Text(
            "Informe Completo de Composición Corporal",
            style={"font-weight": "bold", "font-size": "24px", "margin-bottom": "20px"},
        ),
        # Formulario de entrada
        rx.Input(
            value=MyState.peso, placeholder="Peso (kg)", on_change=MyState.set_peso
        ),
        rx.Input(
            value=MyState.altura,
            placeholder="Altura (cm)",
            on_change=MyState.set_altura,
        ),
        rx.Input(
            value=MyState.edad, placeholder="Edad (años)", on_change=MyState.set_edad
        ),
        rx.Select(
            options=["m", "h"],
            value=MyState.genero,
            on_change=MyState.set_genero,
            placeholder="Género (m para mujer, h para hombre)",
        ),
        rx.Input(
            value=MyState.cuello,
            placeholder="Cuello (cm)",
            on_change=MyState.set_cuello,
        ),
        rx.Input(
            value=MyState.cintura,
            placeholder="Cintura (cm)",
            on_change=MyState.set_cintura,
        ),
        rx.Input(
            value=MyState.cadera,
            placeholder="Cadera (cm, solo para mujeres)",
            on_change=MyState.set_cadera,
        ),
        rx.Select(
            options=["mantener peso", "perder grasa", "ganar masa muscular"],
            value=MyState.objetivo,
            on_change=MyState.set_objetivo,
            placeholder="Objetivo",
        ),
        rx.Button("Calcular", on_click=MyState.obtener_resultado),
        # Área de visualización de resultados
        rx.Text("Resultados:", style={"font-weight": "bold", "margin-top": "20px"}),
        rx.Text(MyState.resultado),  # Muestra el resultado obtenido de la API
    )


app = rx.App()
app.add_page(index)  # Agrega la página principal
app.compile()  # Compila la aplicación
