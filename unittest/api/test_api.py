# Chat test program
# Date: 2024/10/07
# Author: araobp@github.com

import sys
sys.path.append("../../rag")

from urllib import parse

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

        urlparams = parse.urlencode({"query": "Hamburg", "context": "hansaplatz"})
        r = requests.get(f"{BASE_URL}/search?{urlparams}")
        r = r.json()
        print(r)

        self.assertEqual(len(r['ids']), k)
        self.assertEqual(len(r['distances']), k)
        self.assertEqual(len(r['chunks']), k)

    def test_chat(self):
        k = 3

        urlparams = parse.urlencode({"query": "Hamburg", "context": "hansaplatz",
            "user_message": "Where is Hansaplatz?"})
        r = requests.get(f"{BASE_URL}/chat?{urlparams}")
        r = r.json() 
        print(r)

if __name__ == "__main__":
    unittest.main()
