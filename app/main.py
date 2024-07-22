from fastapi import FastAPI
from app.routers.Category_routes import router as category_routes

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(category_routes)
