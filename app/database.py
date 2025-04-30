from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://mongo:27017"
DATABASE_NAME = "local_ai_agent_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

questions_collection = db["questions"]