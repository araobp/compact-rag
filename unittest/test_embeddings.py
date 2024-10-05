# Embeddings test program
# Date: 2024/10/05
# Author: araobp@github.com

import sys
sys.path.append("../rag")

import embeddings 
import unittest

TEXTS = ["hello!", "how are you?", "I'm fine, thank you!"]

class TestEmbeddings(unittest.TestCase):
    """Test embeddings package
    """

    def test_get_embedding(self):
        vector = embeddings.get_embedding(TEXTS[0])
        self.assertEqual(len(vector), embeddings.DIMENSION)
        
        vectors = embeddings.get_embedding(TEXTS)
        self.assertEqual(len(vectors), len(TEXTS))

if __name__ == "__main__":
    unittest.main()
