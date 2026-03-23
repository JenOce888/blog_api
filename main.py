from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router

# Create all tables in the database automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    description="API backend pour gérer un blog simple",
    version="1.0.0"
)

# Register the routes
app.include_router(router)