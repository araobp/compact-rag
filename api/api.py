import sys
sys.path.append("../rag")

from flask import Flask, jsonify

import embeddings
import vector_db

DB_PATH = "../db/documents.db"
VECTOR_DB_PATH = "../db/embeddings.db"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/query")
def chat():
    text = request.args.get("query", default=None, type=str)
    context = request.args.get("context", default=None, type=str)
    collection = vector_db.VectorDB(VECTOR_DB_PATH, context, embeddings.DIMENSION)
    vector = embeddings.get_embedding(text)
    result = collection.search(vector, k=3)
    
    ids = [e[0] for e in result]
    return(jsonify(print(ids)))


if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0', port=5050)
