from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.crud.patient_details import *
from app.server.models.patient_details import *

patient_detail_route = APIRouter()

# Add Patient Details
@patient_detail_route.post("/patient_details", response_description="Patient Detail added into the database")
async def add_student_data(patient_detail_in: BasePatientDetails = Body(...)):
    patient_detail_in = jsonable_encoder(patient_detail_in)
    new_patient_detail = await add_patient_detail(patient_detail_in)
    return ResponseModel(new_patient_detail, "Patient Detail added successfully.")

# Get all Patient Details
@patient_detail_route.get("/patient_details", response_description="Patient Details retrieved")
async def get_patient_details():
    patient_details = await retrieve_patient_details()
    return ResponseModel(patient_details, "Patient Detailsretrieved successfully")

# Get one Patient Detail
@patient_detail_route.get("/patient_details/{id}", response_description="Patient Detail retrieved")
async def get_patient_detail(id):
    patient_detail = await retrieve_patient_detail(id)
    if patient_detail:
        return ResponseModel(patient_detail, "Patient Detail retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Patient Detail doesn't exist.")


@patient_detail_route.put("/patient_details/{id}")
async def put_patient_detail(id: str, req: UpdatePatientDetails = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_patient_detail = await update_patient_detail(id, req)
    if updated_patient_detail:
        return ResponseModel(
            "Patient Detail with ID: {} update is successful".format(id),
            "Patient Detail updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )

# Delete one Patient Detail
@patient_detail_route.delete("/patient_details/{id}", response_description="Patient Detail deleted from the database")
async def delete_patient_detail_func(id: str):
    # print("patient detail delete: ", id)
    deleted_patient_detail = await delete_patient_detail(id)
    if deleted_patient_detail:
        return ResponseModel(
            "Patient Detail with ID: {} removed".format(id), "Patient Detail deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Patient Detail with id {0} doesn't exist".format(id)
    )