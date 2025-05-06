from typing import Union
import json
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Permite todas as origens
    allow_credentials=False,   # Tem que ser False com "*"
    allow_methods=["*"],       # Todos os métodos permitidos
    allow_headers=["*"],       # Todos os headers permitidos
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/heapsort")
def validate_list(array_example):
    numbers_list = json.loads(array_example)
    for i in enumerate(numbers_list):
        if not isinstance(numbers_list[i], int):
            return {"Lista tá errada paizao"}

def list_to_backend(numbers_list):
    if validate_list(array_example='[1, 2, 3, 4, 5]'):
        return numbers_list
    
def backend_to_frontend(sorted_array):
    return json.dump(sorted_array)
