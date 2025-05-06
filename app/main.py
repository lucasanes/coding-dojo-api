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
  if not isinstance(array_example, list) or not all(isinstance(i, int) for i in array_example):
    return {"error": "A lista deve conter apenas números inteiros"}

  try:
    response = requests.post(FLASK_BACKEND_URL, json={"array": array_example})
    if response.status_code == 200:
      sorted_array = response.json().get("sorted_array")
      return {sorted_array}
    else:
      return {
        "error": "Erro no backend Flask",
        "status": response.status_code,
        "body": response.text,
      }
  except Exception as e:
    return {"error": "Falha na conexão com o backend", "details": str(e)}