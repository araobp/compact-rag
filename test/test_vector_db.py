# VectorDB test program
# Date: 2024/10/03
# Author: araobp@github.com

import sys
sys.path.append("../rag")

import embeddings
import vector_db

EMBEDDINGS_DB_PATH = "./test.db"

TEXTS = ["hello!", "how are you?", "I'm fine, thank you!"]

COLLECTION = "hello"

# Instantiate a collection
vectorDB = vector_db.VectorDB(EMBEDDINGS_DB_PATH, COLLECTION, embeddings.DIMENSION)

# Remove all items in the collection
vectorDB.delete_all()

# Calculate and save embeddings in the vector database
items = []

for idx, text in enumerate(TEXTS):
    vector = embeddings.get_embedding(text)
    items.append((idx, vector))

vectorDB.save(items)

# Perform similarity search
text = TEXTS[1]
vector = embeddings.get_embedding(text)
print(text)
print(vectorDB.search(vector))

