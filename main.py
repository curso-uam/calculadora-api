# main.py
"""
Autor José Luis Quiroz Fabián (JLQF)

API REST básica de calculadora usando FastAPI.

Incluye operaciones de suma y factorial de un número.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Calculadora API FastAPI", description="API para operaciones básicas", version="1.0")

class Request(BaseModel):
    a: float
    b: float

@app.get("/")
def inicio():
    """
    Mensaje de bienvenida.
    """
    return {"mensaje": "Bienvenido a la Calculadora API"}

@app.post("/suma")
def suma(datos: Request):
    """
    Realiza la suma de dos números.

    Parámetros:
    - a (float): primer número
    - b (float): segundo número

    Retorna:
    - resultado (float): suma de a y b
    """
    resultado = datos.a + datos.b
    return {"resultado": resultado}

@app.post("/resta")
def resta(datos: Request):
    """
    Realiza la resta de dos números.

    Parámetros:
    - a (float): primer número
    - b (float): segundo número

    Retorna:
    - resultado (float): resta de a y b
    """
    resultado = datos.a - datos.b
    return {"resultado": resultado}

@app.post("/multiplicacion")
def multiplicacion(datos: Request):
    """
    Realiza la multiplicacion de dos números.

    Parámetros:
    - a (float): primer número
    - b (float): segundo número

    Retorna:
    - resultado (float): multiplicacion de a y b
    """
    resultado = datos.a * datos.b
    return {"resultado": resultado}

@app.get("/factorial/{n}")
def factorial(n: int):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    - n (int): número entero

    Retorna:
    - resultado (int): factorial de n

    Lanza:
    - HTTPException si el número es negativo
    """
    if n < 0:
        raise HTTPException(status_code=400, detail="El número debe ser no negativo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return {"resultado": resultado}

