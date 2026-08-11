from fastapi import FastAPI

from routers import chat,todo

app = FastAPI()


##Routers
app.include_router(chat.router)
app.include_router(todo.router)