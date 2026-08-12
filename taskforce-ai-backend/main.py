from fastapi import FastAPI

from routers import chat_router, todo, productivity_router, graph_analyzer

app = FastAPI()


##Routers
app.include_router(chat_router.router)
app.include_router(todo.router)
app.include_router(productivity_router.router)
app.include_router(graph_analyzer.router)