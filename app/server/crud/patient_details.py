from app.server.db.base import database, client
from fastapi import FastAPI, HTTPException
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError


clinical_facility_name = "apollo"
collection_name = clinical_facility_name + "_patient_details"
patient_details_collection = database.get_collection(collection_name)

# helpers
def patient_details_helper(patient_details) -> dict:
    return {
        "id": str(patient_details["_id"]),
        "patient_id_mrn": patient_details["patient_id_mrn"],
        "first_name": patient_details["first_name"],
        "last_name": patient_details["last_name"],
        "email": patient_details["email"],
        "country_code": patient_details["country_code"],
        "mobile": str(patient_details["mobile"]),
        "dob": patient_details["dob"],
        "age": patient_details["age"],
        "sex": patient_details["sex"],
        "weight": patient_details["weight"],
        "height": patient_details["height"],
        "country": str(patient_details["country"]),
        "zip_code": patient_details["zip_code"],
        "street_address_1": patient_details["street_address_1"],
        "street_address_2": patient_details["street_address_2"],
        "city": patient_details["city"],
        "state": patient_details["state"],
        "em_contact_name": patient_details["em_contact_name"],
        "em_contact_country_code": patient_details["em_contact_country_code"],
        "em_contact_number": patient_details["em_contact_number"],
        "created_by": patient_details["created_by"],
    }




# crud operations

# Retrieve all patient details present in the database
async def retrieve_patient_details():
    try:
        patient_details_list = []
        async for patient in patient_details_collection.find():
            patient_details_list.append(patient_details_helper(patient))
        if not patient_details_list:
            raise HTTPException(status_code=404, detail="Patient Details list is Empty")
        return patient_details_list
    except PyMongoError:
        raise HTTPException(status_code=500, detail="Database error")


# Add a new patient Detail into to the database
async def add_patient_detail(patient_detail_in: dict) -> dict:
    try:
        patient_detail = await patient_details_collection.insert_one(patient_detail_in)
        new_patient_detail = await patient_details_collection.find_one({"_id": patient_detail.inserted_id})
        if new_patient_detail is None:
            raise HTTPException(status_code=404, detail="Patient Detail not found")
        return patient_details_helper(new_patient_detail)
    except PyMongoError:
        raise HTTPException(status_code=500, detail="Database error")


# Retrieve a patient detail with a matching ID
async def retrieve_patient_detail(id: str) -> dict:
    try:
        patient_detail = await patient_details_collection.find_one({"_id": ObjectId(id)})
        if patient_detail is None:
            raise HTTPException(status_code=404, detail="Patient Detail not found")
        return patient_details_helper(patient_detail)
    except PyMongoError:
        raise HTTPException(status_code=500, detail="Database error")



# # Update a student with a matching ID
# async def update_student(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         updated_student = await student_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_student:
#             return True
#         return False

# Update a Patient Detail with a matching ID
async def update_patient_detail(id: str, data: dict):
    try:
        # Use optimistic concurrency control with the find_one_and_update method
        updated_patient_detail = await patient_details_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": data},
            return_document=True
        )

        if updated_patient_detail is None:
            raise HTTPException(status_code=404, detail="Patient Detail not found")

        return updated_patient_detail

    except PyMongoError:
        raise HTTPException(status_code=500, detail="Database error")


    # try:
    #     # Return false if an empty request body is sent.
    #     if len(data) < 1:
    #         return False
    #     patient_detail = await patient_details_collection.find_one({"_id": ObjectId(id)})
    #     if patient_detail is None:
    #         raise HTTPException(status_code=404, detail="Patient Detail data not found")
    #     # Perform the update within a transaction
    #     with client.start_session() as session:
    #         with client.start_transaction():
    #             updated_patient_detail = await patient_details_collection.update_one(
    #                 {"_id": ObjectId(id)}, {"$set": data}
    #             )
    #             if session.has_ended:
    #                 # The transaction was aborted, possibly due to concurrent modification
    #                 raise HTTPException(status_code=409, detail="Conflict")
    # except PyMongoError:
    #     # Handle any MongoDB-specific exceptions
    #     raise HTTPException(status_code=500, detail="Database error")
    
    # return updated_patient_detail



# Delete a patient_detail from the database
async def delete_patient_detail(id: str):
    patient_detail = await patient_details_collection.find_one({"_id": ObjectId(id)})
    if patient_detail:
        await patient_details_collection.delete_one({"_id": ObjectId(id)})
        return True