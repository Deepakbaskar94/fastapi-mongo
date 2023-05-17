import motor.motor_asyncio
# from decouple import config

# MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

# MONGO_DETAILS = 'mongodb://root:root123$@127.0.0.1:27017'
# MONGO_DETAILS = 'mongodb://root:root123$@127.0.0.1:27017'
MONGO_DETAILS = 'mongodb://root:root123$@ecg-mongo-mongodb-1:27017'


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.first