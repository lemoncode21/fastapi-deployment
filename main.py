import uvicorn
from fastapi import FastAPI
from config import db


def init_app():
    app = FastAPI()

    @app.get("/")
    def home():
        return "Welcome Home"

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    from controller import router
    app.include_router(router)

    return app


app = init_app()

