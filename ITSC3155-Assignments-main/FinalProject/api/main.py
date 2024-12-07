import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dependencies.config import conf
from .models import model_loader
from .routers import index as indexRoute
from .routers import menu_items
from .routers import order_management

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)


app.include_router(menu_items.router)
app.include_router(order_management.router)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)