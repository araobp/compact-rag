# Chat test program
# Date: 2024/10/07
# Author: araobp@github.com

import sys
sys.path.append("../../rag")

from urllib import parse

import requests 
import base64
import unittest

BASE_URL = "http://localhost:5050"

IMG_PATH1 = "./image/0_iso-republic-cat-bathing.jpg"
IMG_PATH2 = "./image/IMG_0230_level.jpg"

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

        urlparams = parse.urlencode({
            "context": "hansaplatz",
            "user_message": "Where is Hansaplatz?"
            })
        r = requests.get(f"{BASE_URL}/search?{urlparams}")
        r = r.json()
        print(r)

        self.assertEqual(len(r['ids']), k)
        self.assertEqual(len(r['distances']), k)
        self.assertEqual(len(r['chunks']), k)

    def test_chat(self):
        k = 3

        urlparams = parse.urlencode({
            "context": "hansaplatz",
            "user_message": "Where is Hansaplatz?"
            })
        r = requests.get(f"{BASE_URL}/chat?{urlparams}")
        r = r.json() 
        print(r)

    def test_chat_with_image(self):
        k = 3

        with open(IMG_PATH2, 'rb') as f:
            b64image = base64.b64encode(f.read())

        urlparams = parse.urlencode({
            "context": "yokohama",
            "user_message": "What are the histric buildings in the left hand in the image?"
            })
        r = requests.put(f"{BASE_URL}/chat?{urlparams}", json={"b64image": b64image})
        r = r.json()
        print(r)

if __name__ == "__main__":
    unittest.main()
