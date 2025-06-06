# Calculadora API con FastAPI

Este proyecto es una API REST sencilla que implementa operaciones básicas de una calculadora, desarrollada con **FastAPI**.

## Características

-Suma de dos números (`POST /suma`)
-Cálculo del factorial de un número entero no negativo (`GET /factorial/{n}`)
-Documentación automática disponible en Swagger UI (`/docs`)

## Requisitos previos

- Python 3.8 o superior
- pip (administrador de paquetes de Python)

## Instalación y ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/curso-uam/calculadora-api.git
   cd calculadora-api
   pip install -r requirements.txt 

2. Ejecuta la API:
   uvicorn main:app --reload

3. Prueba la API
   http://127.0.0.1:8000/docs

    
