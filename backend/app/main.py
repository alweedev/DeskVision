from fastapi import FastAPI
from app.database.connection import Base, engine
from app.models import user, ticket

app = FastAPI(
    title="Helpdesk API",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API is running"}
