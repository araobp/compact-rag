# Chat test program
# Date: 2024/10/09
# Author: araobp@github.com

import sys
sys.path.append("../../rag")

from urllib import parse

import requests 
import base64
import unittest

BASE_URL = "http://localhost:5050"


class TestChat(unittest.TestCase):
    """Test the APIs
    """

    def test_chat_with_onboard_webcam_without_context(self):

            urlparams = parse.urlencode({
                "user_message": "What can you see in the attached image?",
                })
            r = requests.get(f"{BASE_URL}/chat?{urlparams}&use_webcam=true")
            self.assertEqual(r.status_code, 200)

            print(r.json()['answer'])
            b64image = r.json()['b64image']
            jpg_img = base64.b64decode(b64image) 

            with open("./tmp/cap.jpg", "wb") as f:
                f.write(jpg_img)


if __name__ == "__main__":
    unittest.main()
