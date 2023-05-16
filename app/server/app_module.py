from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from server.routes.user import user_route
# from server.routes.item import item_route
from server.routes.student import router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(user_route)
# app.include_router(item_route)
app.include_router(router)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}