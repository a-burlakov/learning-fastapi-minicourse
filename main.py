import uvicorn
from fastapi import FastAPI
from database import engine, Base
from routers import user as UserRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserRouter.router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("mainapp", host="0.0.0.0", port=8080, reload=True, workers=3)
