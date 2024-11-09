# Componente de formulario para ingresar datos
# components/form_component.py
import reflex as rx
from state.my_state import MyState


def form_component():
    return rx.Container(
        rx.Input(value=MyState.peso, placeholder="Peso", on_change=MyState.peso),
        rx.Input(value=MyState.altura, placeholder="Altura", on_change=MyState.altura),
        rx.Input(value=MyState.edad, placeholder="Edad", on_change=MyState.edad),
        rx.Select(
            options=["m", "h"],
            value=MyState.genero,
            on_change=MyState.genero,
            placeholder="Género",
        ),
        rx.Input(value=MyState.cuello, placeholder="Cuello", on_change=MyState.cuello),
        rx.Input(
            value=MyState.cintura, placeholder="Cintura", on_change=MyState.cintura
        ),
        rx.Input(value=MyState.cadera, placeholder="Cadera", on_change=MyState.cadera),
        rx.Select(
            options=["mantener peso", "perder grasa", "ganar masa muscular"],
            value=MyState.objetivo,
            on_change=MyState.objetivo,
            placeholder="Objetivo",
        ),
        rx.Button("Calcular", on_click=MyState.obtener_resultado),
    )
