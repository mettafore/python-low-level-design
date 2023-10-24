# import uvicorn
from fastapi import FastAPI
from controllers.UserController import user_router
# from controllers.AdminController import admin_router
# from controllers.OrderController import order_router
# from controllers.BooksController import book_router
# from controllers.ExploreController import explore_router
from controllers.HealthController import health_router
from fastapi.middleware.cors import CORSMiddleware
# from framework.initial_setup import initial_setup, delete_all_tables
from os.path import join
from dotenv import load_dotenv
from framework.initial_setup import initial_setup

load_dotenv(join("config", ".env"))
app = FastAPI()

origins = ['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(user_router)
app.include_router(health_router)
# app.include_router(admin_router)
# app.include_router(order_router)
# app.include_router(book_router)
# app.include_router(explore_router)


# Initial Setup
# delete_all_tables()
initial_setup()