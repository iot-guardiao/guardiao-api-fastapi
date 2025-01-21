from fastapi import FastAPI
from api.v1.agendamento.controller import router as agendamento_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(agendamento_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Guardião API"}
