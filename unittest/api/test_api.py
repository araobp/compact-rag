# Chat test program
# Date: 2024/10/07
# Author: araobp@github.com

import sys
sys.path.append("../../rag")

import requests 
import unittest

BASE_URL = "http://localhost:5050"

class TestChat(unittest.TestCase):
    """Test the APIs
    """

    def test_chat(self):
        r = requests.get(BASE_URL)
        r = r.json()
        print(r)
        self.assertEqual(type(r['message']), str)

    def test_search(self):
        k = 3

        r = requests.get(f"{BASE_URL}/search?query=Hamburg&context=hansaplatz")
        r = r.json()
        print(r)

        self.assertEqual(len(r['ids']), k)
        self.assertEqual(len(r['distances']), k)
        self.assertEqual(len(r['chunks']), k)

if __name__ == "__main__":
    unittest.main()
