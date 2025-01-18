from fastapi import FastAPI
from api.v1.agendamento.controller import router as agendamento_router

app = FastAPI()
app.include_router(agendamento_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Guardião API"}
