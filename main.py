from fastapi import FastAPI
from routers.user_router import router
from routers.auth_router import router as auth_router
from middlewares.logging_middleware import LoggingMiddleware
from exceptions.global_exception import global_exception_handler
app = FastAPI()

app.add_middleware(LoggingMiddleware)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(router)
app.include_router(auth_router)