# webcam 
#
# Author: araobp@github.com
# Date: 2024/10/10

import cv2
import base64

IMG_CAP_HEIGHT = 720
IMG_CAP_WIDTH = 1280

IMG_TARGET_HEIGHT = 512
IMG_TARGET_WIDTH = int(IMG_TARGET_HEIGHT / IMG_CAP_HEIGHT * IMG_CAP_WIDTH)

SKIP_FRAMES = 8  # For the camera to adjust to light

def capture():
    """Capture image from USB webcam connected to Raspberry Pi.

    Webcam: Buffalo BSW200MBK
    https://www.buffalo.jp/product/detail/bsw200mbk.html

    This function should work with other webcam models, since it is a standard USB camera.
    """

    # Video Capture from USB Webcam
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    for i in range(SKIP_FRAMES):
        result, img = cap.read()

    result, img = cap.read()

    cap.release()
    
    if result is False:
        raise Exception("Video capture failed")
    else:
        img_resized = cv2.resize(img, (IMG_TARGET_WIDTH, IMG_TARGET_HEIGHT))
        retval, jpg_img= cv2.imencode('.jpg', img_resized)
        b64image = base64.b64encode(jpg_img).decode('utf-8')
        return b64image

