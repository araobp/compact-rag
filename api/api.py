import sys
sys.path.append("../rag")

from flask import Flask, jsonify, request
import sqlite3

import embeddings
import vector_db

DB_PATH = "../db/documents.db"
VECTOR_DB_PATH = "../db/embeddings.db"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route("/search")
def search():
    text = request.args.get("query", default=None, type=str)
    context = request.args.get("context", default=None, type=str)
    k = request.args.get("k", default=3, type=int)

    collection = vector_db.VectorDB(VECTOR_DB_PATH, context, embeddings.DIMENSION)
    vector = embeddings.get_embedding(text)
    result = collection.search(vector, k=k)
    
    ids = [e[0] for e in result]
    ids_str = [str(e[0]) for e in result]
    ids_str = f"{','.join(ids_str)}"
    
    distances = [e[1] for e in result]

    sql = f'SELECT id, chunk FROM chunks WHERE collection="{context}" AND id IN ({ids_str})'

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        records = cur.execute(sql).fetchall()

    records_ = {}
    for r in records:
        id_ = r[0]
        chunk = r[1]
        records_[id_] = chunk

    chunks = [records_[idx] for idx in ids]

    return(jsonify({"ids": ids, "distances": distances, "chunks": chunks}))


if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=5050)
