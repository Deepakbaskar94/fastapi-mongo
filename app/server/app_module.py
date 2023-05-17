from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from server.routes.user import user_route
# from server.routes.item import item_route
from app.server.routes.patient_details import patient_detail_route

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(patient_detail_route)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}