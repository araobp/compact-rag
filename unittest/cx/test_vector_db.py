# VectorDB test program
# Date: 2024/10/03, 2025/01/26
# Author: araobp@github.com

import sys
sys.path.append("../..")

from cx.rag import embeddings, vector_db
import unittest

EMBEDDINGS_DB_PATH = "./test.db"

TEXTS = {
        "contexts": ["A", "A", "B"],
        "chunks": ["hello!", "how are you?", "I'm fine, thank you!"]
        }

COLLECTION = "hello"

class TestVectorDB(unittest.TestCase):
    """Test vector_db package
    """

    def _collection(self):
        return vector_db.VectorDB(EMBEDDINGS_DB_PATH, COLLECTION, embeddings.DIMENSION)

    def _embeddings(self):
        items = []

        for idx, chunk in enumerate(TEXTS["chunks"]):
            vector = embeddings.get_embedding(chunk)
            context = TEXTS["contexts"][idx]
            items.append((context, vector, chunk))

        return items
         
    def  test_instantiate(self):
        """Instantiate a collection
        """
        collection = self._collection() 
        self.assertEqual(type(collection), vector_db.VectorDB)

    def test_delete_all(self):
        """Remove all items in the collection
        """
        collection = self._collection() 
        collection.delete_all()
        items = self._embeddings()
        collection.save(items)
        self.assertEqual(len(collection), len(TEXTS["chunks"]))
        collection.delete_all()
        self.assertEqual(len(collection), 0)

    def test_save_embedding(self):
        """Calculate and save embeddings in the vector database
        """
        collection = self._collection() 
        collection.delete_all()
        items = self._embeddings() 
        collection.save(items)
        self.assertEqual(len(collection), len(TEXTS["chunks"]))

    def test_similarity_search(self):
        """Perform similarity search
        """
        collection = self._collection() 
        query = TEXTS["chunks"][1]
        context = TEXTS["contexts"][1]
        print(f"Text to be searched: {query}, context: {context}")
        vector = embeddings.get_embedding(query)
        
        result = collection.search(vector, context)
        print(f"Search result(k=3): {result}")
        self.assertEqual(result[0][0], query)
        self.assertEqual(len(result), 2)

        result = collection.search(vector, context, k=1)
        print(f"Search result(k=1): {result}")
        self.assertEqual(result[0][0], query)
        self.assertEqual(len(result), 1)
    
if __name__ == "__main__":
    unittest.main()

