# Embeddings calcuration for the chunks
# Date: 2024/10/06, 2025/01/26
# Author: araobp@github.com

import sys
sys.path.append("..")
sys.path.append("../cx")

import sqlite3
from rag import vector_db
from rag import embeddings

DB_PATH = "../db/documents.db"
VECTOR_DB_PATH = "../db/embeddings.db"

# Read all the chunks
with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    records = cur.execute("SELECT collection, context, chunk FROM chunks").fetchall()

data = {}

for r in records:
    collection = r[0]
    if collection not in data:
        data[collection] = []
    data[collection].append([r[1], r[2]])

N = 10  # Batch size for embeddings calculation

records = {} 

# Calculate embeddings
for collection in data.keys():
    print(f"Collection: {collection}")
    items = data[collection]
    for i in range(0, len(items), N):
        contexts, chunks = zip(*items[i:i+N])
        print(contexts[0])
        vectors = embeddings.get_embedding(chunks)
        if collection not in records:
            records[collection] = []
        records[collection].extend(zip(contexts, vectors, chunks))

# Save the embeddings in a vector database
print("Saving the data in the database...")
for collection, items in records.items():
    col_db = vector_db.VectorDB(VECTOR_DB_PATH, collection, embeddings.DIMENSION)
    col_db.save(items)
