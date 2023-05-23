from datastore.datastore import DataStore
from datastore.providers.pinecone_datastore import PineconeDataStore


async def get_datastore() -> DataStore:
    return PineconeDataStore()
