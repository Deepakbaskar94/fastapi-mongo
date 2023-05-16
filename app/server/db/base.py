# from motor.motor_asyncio import AsyncIOMotorClient


# # Connect to MongoDB
# client = AsyncIOMotorClient("mongodb://localhost:27017")
# db = client["first"]

import motor.motor_asyncio
# from decouple import config

# MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

MONGO_DETAILS = 'mongodb://root:root123$@127.0.0.1:27017'


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.first