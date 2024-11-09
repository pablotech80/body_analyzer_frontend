# api_requests.py
import reflex as rx


def obtener_datos(datos):
    response = rx.fetch(
        url=f"{rx.config.api_url}/informe_completo",
        method="POST",
        json=datos,
    )
    return response.json() if response else None
