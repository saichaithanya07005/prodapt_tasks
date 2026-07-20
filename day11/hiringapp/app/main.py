from fastapi import FastAPI

from app.core.database import Base, engine

# Import models so SQLAlchemy registers them
from app.models.job import Job

app = FastAPI(
    title="Hiring Application"
)

# Create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Hiring Application Started Successfully"
    }
