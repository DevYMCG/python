from fastapi import FastAPI

app = FastAPI()

# path de la ruta
@app.get("/")
def home():
    return {"Hello": "world"}