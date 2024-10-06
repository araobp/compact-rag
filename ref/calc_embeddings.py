# Embeddings calcuration for the chunks
# Date: 2024/10/06
# Author: araobp@github.com

import sys
sys.path.append("../rag")

import sqlite3
import embeddings
import vector_db

DB_PATH = "../db/documents.db"
VECTOR_DB_PATH = "../db/embeddings.db"

# Read all the chunks
with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    records = cur.execute("SELECT id, collection, chunk FROM chunks").fetchall()

data = {}

for r in records:
    collection = r[1]
    if collection not in data:
        data[collection] = []
    data[collection].append([r[0], r[2]])

N = 10  # Batch size for embeddings calculation

records = {} 

# Calculate embeddings
for collection in data.keys():
    print(f"Collection: {collection}")
    items = data[collection]
    for i in range(0, len(items), N):
        ids, chunks = zip(*items[i:i+N])
        vectors = embeddings.get_embedding(chunks)
        if collection not in vectors:
            records[collection] = []
        records[collection].extend(zip(ids, vectors))

# Save the embeddings in a vector database
print("Saving the data in the database...")
for collection, items in records.items():
    col_db = vector_db.VectorDB(VECTOR_DB_PATH, collection, embeddings.DIMENSION)
    col_db.save(items)
