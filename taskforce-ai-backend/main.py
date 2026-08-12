from fastapi import FastAPI

from routers import chat,todo,productivity_router

app = FastAPI()


##Routers
app.include_router(chat.router)
app.include_router(todo.router)
app.include_router(productivity_router.router)