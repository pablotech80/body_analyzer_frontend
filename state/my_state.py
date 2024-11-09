import reflex as rx
import requests


class MyState(rx.State):
    peso = ""
    altura = ""
    edad = ""
    genero = ""
    cuello = ""
    cintura = ""
    cadera = ""
    objetivo = ""
    resultado = ""

    @staticmethod
    def obtener_resultado():
        # Crear el JSON de datos que se enviarán al backend
        data = {
            "peso": MyState.peso,
            "altura": MyState.altura,
            "edad": MyState.edad,
            "genero": MyState.genero,
            "cuello": MyState.cuello,
            "cintura": MyState.cintura,
            "cadera": MyState.cadera,
            "objetivo": MyState.objetivo,
        }
        try:
            # Hacer una solicitud POST al endpoint del backend de Flask
            response = requests.post(
                "http://localhost:5000/informe_completo", json=data
            )
            if response.status_code == 200:
                MyState.resultado = response.json()  # Asigna la respuesta al estado
            else:
                MyState.resultado = "Error en la solicitud al servidor"
        except requests.RequestException as e:
            MyState.resultado = f"Error: {str(e)}"
