# Chat test program
# Date: 2024/10/09
# Author: araobp@github.com

import sys
sys.path.append("../../rag")

from urllib import parse

import requests 
import base64
import cv2
import unittest

BASE_URL = "http://localhost:5050"

IMG_CAP_WIDTH = 1280
IMG_CAP_HEIGHT = 720

IMG_TARGET_HEIGHT = 512
IMG_TARGET_WIDTH = int(IMG_TARGET_HEIGHT / IMG_CAP_HEIGHT * IMG_CAP_WIDTH)

class TestChat(unittest.TestCase):
    """Test the APIs
    """

    def test_chat_with_webcam_image_without_context(self):
        """Webcam: Buffalo BSW200MBK
        https://www.buffalo.jp/product/detail/bsw200mbk.html
        """

        # Video Capture from USB Webcam
        cap = cv2.VideoCapture(0)

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        print(f"[Initial resolution] width: {width}, height: {height}, fps: {fps}")

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(f"[Higher resolution] width: {width}, height: {height}, fps: {fps}")

        result, img = cap.read()

        cap.release()

        if result is False:
            raise Exception("Video capture error!")
        else:

            img_resized = cv2.resize(img, (IMG_TARGET_WIDTH, IMG_TARGET_HEIGHT))
            retval, jpg_img= cv2.imencode('.jpg', img_resized)
            b64image = base64.b64encode(jpg_img).decode('utf-8')

            # with open("./tmp/cap.jpg", "wb") as f:
            #    f.write(jpg_img)

            urlparams = parse.urlencode({
                "user_message": "What can you see in the attached image?",
                })
            r = requests.put(f"{BASE_URL}/chat?{urlparams}",
                json={"b64image": b64image})
            print(r.json())
            self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
