import reflex as rx

config = rx.Config(
    app_name="body_analyzer_frontend",
    api_url="http://127.0.0.1:5000",  # Dirección del backend Flask en el puerto 5000
    frontend_port=3000,  # Puerto para el frontend
)
