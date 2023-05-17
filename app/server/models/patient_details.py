from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from datetime import date

class UserGender(str, Enum):
    male = "M"
    female = "F"
    other = "O"

# TO support creation and update APIs
class BasePatientDetails(BaseModel):
    patient_id_mrn: str
    first_name: str
    last_name: str
    email: str
    country_code: str
    mobile: str
    dob: str
    age: int
    sex: UserGender
    weight: float
    height: float
    country: str
    zip_code: str
    street_address_1: str
    street_address_2: str
    city: str
    state: str
    em_contact_name: str
    em_contact_country_code: str
    em_contact_number: str
    created_by: str

    class Config:
        schema_extra = {
            "example": {
                "patient_id_mrn": "PID_01",
                "first_name": "John",
                "last_name": "Doe",
                "email": "John@gmail.com",
                "country_code": "+91",
                "mobile": "9876543210",
                "dob": "13-11-1994",
                "age": "20",
                "sex": "M",
                "weight": "80.0",
                "height": "175",
                "country": "India",
                "zip_code": "607002",
                "street_address_1": "ajmeer aditya",
                "street_address_2": "koramangala",
                "city": "Bangalore",
                "state": "Karnataka",
                "em_contact_name": "Deepakem",
                "em_contact_country_code": "+91",
                "em_contact_number": "7894561230",
                "created_by": "clinician_id"
            }
        }

class UpdatePatientDetails(BaseModel):
    patient_id_mrn: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    country_code: Optional[str]
    mobile: Optional[str]
    dob: Optional[str]
    age: Optional[int]
    sex: Optional[UserGender]
    weight: Optional[float]
    height: Optional[float]
    country: Optional[str]
    zip_code: Optional[str]
    street_address_1: Optional[str]
    street_address_2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    em_contact_name: Optional[str]
    em_contact_country_code: Optional[str]
    em_contact_number: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "patient_id_mrn": "PID_01",
                "first_name": "Deepak",
                "last_name": "Doe",
                "email": "John@gmail.com",
                "country_code": "+91",
                "mobile": "9876543210",
                "dob": "13-11-1994",
                "age": "20",
                "sex": "M",
                "weight": "80.0",
                "height": "175",
                "country": "India",
                "zip_code": "607002",
                "street_address_1": "ajmeer aditya",
                "street_address_2": "koramangala",
                "city": "Bangalore",
                "state": "Karnataka",
                "em_contact_name": "Deepakem",
                "em_contact_country_code": "+91",
                "em_contact_number": "7894561230"
            }
        }


# class StudentSchema(BaseModel):
#     patient_id_mrn: str = Field(...)
#     first_name: str = Field(...)
#     last_name: str = Field(...)
#     email: int = Field(..., gt=0, lt=9)
#     country_code: float = Field(..., le=4.0)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "John Doe",
#                 "email": "jdoe@x.edu.ng",
#                 "course_of_study": "Water resources engineering",
#                 "year": 2,
#                 "gpa": "3.0",
#             }
#         }


# class UpdateStudentModel(BaseModel):
#     fullname: Optional[str]
#     email: Optional[str]
#     course_of_study: Optional[str]
#     year: Optional[int]
#     gpa: Optional[float]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "John Doe",
#                 "email": "jdoe@x.edu.ng",
#                 "course_of_study": "Water resources and environmental engineering",
#                 "year": 4,
#                 "gpa": "4.0",
#             }
#         }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}