# Componente para mostrar los resultados
# components/result_component.py
import reflex as rx
from state.my_state import MyState


def result_component():
    return rx.Container(
        rx.Text("Resultados:", style={"font-weight": "bold"}),
        rx.Text(MyState.resultado),  # Muestra el resultado
    )
