# main.py
"""
API REST básica de calculadora usando FastAPI.

Incluye operaciones de suma y factorial de un número.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Calculadora API", description="API para operaciones básicas", version="1.0")

class SumaRequest(BaseModel):
    a: float
    b: float

@app.get("/")
def inicio():
    """
    Mensaje de bienvenida.
    """
    return {"mensaje": "Bienvenido a la Calculadora API"}

@app.post("/suma")
def suma(datos: SumaRequest):
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

