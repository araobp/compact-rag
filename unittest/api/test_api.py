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
IMG_PATH3 = "./image/IMG_0230_level_cropped.jpg"

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
            "user_message": "Where is Hansaplatz?",
            "k": k
            })
        r = requests.get(f"{BASE_URL}/chat?{urlparams}")
        print(r.json())
        self.assertEqual(r.status_code, 200)


    def test_chat_with_image(self):
        k = 3

        with open(IMG_PATH3, 'rb') as f:
            b64image = base64.b64encode(f.read()).decode('utf-8')

        urlparams = parse.urlencode({
            "context": "yokohama",
            "user_message": "What can you see in the attached image?",
            "k": k
            })
        r = requests.put(f"{BASE_URL}/chat?{urlparams}",
                json={"b64image": b64image})
        print(r.json())
        self.assertEqual(r.status_code, 200)


    def test_chat_with_image_without_context(self):
        
        with open(IMG_PATH1, 'rb') as f:
            b64image = base64.b64encode(f.read()).decode('utf-8')

        urlparams = parse.urlencode({
            "user_message": "What can you see in the attached image?",
            })
        r = requests.put(f"{BASE_URL}/chat?{urlparams}",
            json={"b64image": b64image})
        print(r.json())
        self.assertEqual(r.status_code, 200)


    def test_tts(self):
        urlparams = parse.urlencode({
            "voice": "alloy",
            "text": "I am going to develop AI Agents."
            })
        r = requests.get(f"{BASE_URL}/tts?{urlparams}")
        speech = r.content
        with open("./tmp/speech.mp3", "wb") as f:
            f.write(speech)
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
