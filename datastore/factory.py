from datastore.datastore import DataStore
import os


async def get_datastore() -> DataStore:
    datastore = os.environ.get("DATASTORE")
    assert datastore is not None

    if datastore == "chroma":
        from datastore.providers.chroma_datastore import ChromaDataStore

        return ChromaDataStore()
    if datastore == "llama":
        from datastore.providers.llama_datastore import LlamaDataStore

        return LlamaDataStore()

    if datastore == "pinecone":
        from datastore.providers.pinecone_datastore import PineconeDataStore

        return PineconeDataStore()
    if datastore == "weaviate":
        from datastore.providers.weaviate_datastore import WeaviateDataStore

        return WeaviateDataStore()
    if datastore == "milvus":
        from datastore.providers.milvus_datastore import MilvusDataStore

        return MilvusDataStore()
    if datastore == "zilliz":
        from datastore.providers.zilliz_datastore import ZillizDataStore

        return ZillizDataStore()
    if datastore == "redis":
        from datastore.providers.redis_datastore import RedisDataStore

        return await RedisDataStore.init()
    if datastore == "qdrant":
        from datastore.providers.qdrant_datastore import QdrantDataStore

        return QdrantDataStore()
    if datastore == "azuresearch":
        from datastore.providers.azuresearch_datastore import AzureSearchDataStore

        return AzureSearchDataStore()
    if datastore == "supabase":
        from datastore.providers.supabase_datastore import SupabaseDataStore

        return SupabaseDataStore()
    if datastore == "postgres":
        from datastore.providers.postgres_datastore import PostgresDataStore

        return PostgresDataStore()

    raise ValueError(
        f"Unsupported vector database: {datastore}. "
        f"Try one of the following: llama, pinecone, weaviate, milvus, zilliz, redis, or qdrant"
    )
