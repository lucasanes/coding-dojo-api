from typing import List
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import json
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

FLASK_BACKEND_URL = "https://coding-dojo-backend.lucasanes.com/heapsort"

@app.post("/heapsort")
def process_array(array_example: List[int] = Body(...)):
    try:
        # Converte string JSON em lista Python
        numbers_list = json.loads(array_example)
    except json.JSONDecodeError:
        return {"error": "JSON inválido"}

    # Validação: deve ser lista de inteiros
    if not isinstance(numbers_list, list) or not all(isinstance(i, int) for i in numbers_list):
        return {"error": "A lista deve conter apenas números inteiros"}

    # Envia para o backend Flask
    try:
        response = requests.post(FLASK_BACKEND_URL, json={"array": numbers_list})
        if response.status_code == 200:
            sorted_array = response.json().get("sorted_array")
            return sorted_array  # <-- Aqui retornamos diretamente como array JSON
        else:
            return {"error": "Erro no backend Flask", "status": response.status_code}
    except Exception as e:
        return {"error": "Falha na conexão com o backend", "details": str(e)}
