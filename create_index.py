import os
import pinecone
from dotenv import load_dotenv

load_dotenv()
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")
)

index_name = "azr-knowledge"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine"
    )
    print(f"✅ Created index '{index_name}'")
else:
    print(f"✅ Index '{index_name}' already exists")
