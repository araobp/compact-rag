# Embeddings test program
# Date: 2024/10/05
# Author: araobp@github.com

import sys
sys.path.append("../rag")

import embeddings 
import unittest

TEXTS1 = ["hello!", "how are you?", "I'm fine, thank you!"]
TEXTS2 = ("hello!", "how are you?", "I'm fine, thank you!")

class TestEmbeddings(unittest.TestCase):
    """Test embeddings package
    """

    def test_get_embedding(self):
        vector = embeddings.get_embedding(TEXTS1[0])
        self.assertEqual(len(vector), embeddings.DIMENSION)
        
        vectors = embeddings.get_embedding(TEXTS1)
        self.assertEqual(len(vectors), len(TEXTS1))

        vectors = embeddings.get_embedding(TEXTS2)
        self.assertEqual(len(vectors), len(TEXTS2))
 
if __name__ == "__main__":
    unittest.main()
