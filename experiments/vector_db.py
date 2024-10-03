import struct
from typing import List

LIB_PATH = "../lib"

#---- Reference: sqlite_vec __init__.py 

from os import path
import sqlite3

__version__ = "0.1.3"
__version_info__ = tuple(__version__.split("."))

def loadable_path():
    """ Returns the full path to the sqlite-vec loadable SQLite extension bundled with this package """

    #loadable_path = path.join(path.dirname(__file__), "vec0")
    loadable_path = path.join(LIB_PATH, "vec0") 
    return path.normpath(loadable_path)

def load(conn: sqlite3.Connection)  -> None:
  """ Load the sqlite-vec SQLite extension into the given database connection. """

  conn.load_extension(loadable_path())

#---- The code below is my original

def serialize_f32(vector: List[float]) -> bytes:
    """serializes a list of floats into a compact "raw bytes" format"""
    return struct.pack("%sf" % len(vector), *vector)


class VectorDB:

    def __init__(self, db_path, collection, dimensions):
        self.db_path = db_path
        self.db = sqlite3.connect(db_path)
        self.db.enable_load_extension(True)
        #sqlite_vec.load(self.db)
        load(self.db)
        self.db.enable_load_extension(False)
        self.db.execute(
            f"CREATE VIRTUAL TABLE IF NOT EXISTS {collection} USING vec0(embedding float[{dimensions}])"
        )
        self.collection = collection

    def delete_all(self):
        with self.db:
            self.db.execute(f"DELETE FROM {self.collection}")

    def save(self, items):
        with self.db:
            self.db.executemany(
                f"INSERT INTO {self.collection}(rowid, embedding) VALUES (?, ?)",
                [[item[0], serialize_f32(item[1])] for item in items],
            )

    def search(self, query, k=10):
        rows = self.db.execute(
            f"SELECT rowid, distance FROM {self.collection} WHERE embedding MATCH ? AND k = {k} ORDER BY distance",
            [serialize_f32(query)],
        ).fetchall()
        return rows


if __name__ == "__main__":
    EMBEDDINGS_DB_PATH = "./test.db"

    items = [
        (1, [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),
        (2, [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]),
        (3, [0.3, 0.3, 0.3, 0.3, 0.3, -0.3]),
        (4, [0.4, 0.4, 0.4, 0.4, 0.4, 0.4]),
        (5, [0.5, 0.5, 0.5, 0.5, 0.5, -0.5]),
    ]
    query = [0.3, 0.3, 0.3, 0.3, 0.3, -0.3]

    vectorDB = VectorDB(EMBEDDINGS_DB_PATH, "test", 6)
    vectorDB.delete_all()
    vectorDB.save(items)
    print(vectorDB.search(query))
