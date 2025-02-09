import os
import sys
import syslog

from flask import Flask, Blueprint, jsonify, request, make_response, render_template
import sqlite3

import sys
sys.path.append("..")

from cx.rag import chat, embeddings, vector_db, tts
from cx.devices import webcam

main = Blueprint("main", __name__)

SAVE_IMAGE = False
SAVE_AUDIO = False

VECTOR_DB_PATH = "../db/embeddings.db"
COLLECTION = "virtual_showroom"

# OpenAI's Text-to-Speech
tts_alloy = tts.TTS(voice="alloy", format="mp3")
tts_nova = tts.TTS(voice="nova", format="mp3")
voices = {"alloy": tts_alloy, "nova": tts_nova}

app = Flask(__name__)


def _search(text, context, k):

    collection = vector_db.VectorDB(VECTOR_DB_PATH, COLLECTION, embeddings.DIMENSION)
    vector = embeddings.get_embedding(text)
    records = collection.search(vector, context, k=k)
    chunks = [e[0] for e in records]
    distances = [e[1] for e in records]
    
    result = {"chunks": chunks, "distances": distances}
    syslog.syslog(f"{text}: {result['chunks'][0]}")
    return result


@main.route("/")
def index_page():
    return render_template("index.html")


@main.route("/webcam")
def webcam_page():
    return render_template("webcam.html")
 

@main.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})


@main.route("/search", methods=["GET"])
def search():
    user_message = request.args.get("user_message", default=None, type=str)
    context = request.args.get("context", default=None, type=str)
    k = request.args.get("k", default=3, type=int)

    return(jsonify(_search(user_message, context, k)))


@main.route("/chat", methods=["GET", "PUT"])
def chat_():
    system_message = request.args.get("system_message", default=chat.DEFAULT_SYSTEM_MESSAGE, type=str)
    user_message = request.args.get("user_message", default=None, type=str)
    context = request.args.get("context", default=None, type=str)
    k = request.args.get("k", default=3, type=int)
    json_output = request.args.get("json_output", default="false", type=str)
    use_webcam = request.args.get("use_webcam", default="false", type=str)

    json_output = True if json_output == "true" else False
    use_webcam = True if use_webcam == "true" else False

    def _save_img(b64image):
       with open("./tmp/b64image.txt", "w") as f:
            f.write(b64image)

    if request.method == "PUT":
        data = request.json
        b64image = data["b64image"]
        if SAVE_IMAGE:
            _save_img(b64image)
    elif use_webcam:
        b64image = webcam.capture()
        if SAVE_IMAGE:
            _save_img(b64image)
    else:
        b64image = None

    result = _search(user_message, context, k) if context is not None else None

    chunks = '\n\n'.join(result['chunks']) if context is not None else None

    prompt = f'''Please refer to the attached document and respond to the following instructions.

## Question

{user_message}

## Attached document

{chunks}
''' if context is not None else user_message

    response = chat.invoke(
            user_message=prompt,
            system_message=system_message,
            b64image=b64image,
            json_output=json_output
            )

    if use_webcam:
        return(jsonify({"answer": response, "b64image": b64image}))
    else:
        return(jsonify({"answer": response}))
    

@main.route("/tts", methods=["GET"])
def text_to_speech():
    voice = request.args.get("voice", default="alloy", type=str)
    text = request.args.get("text", default="hello", type=str)

    speech = voices[voice].speak(text)
    if SAVE_AUDIO:
        with open("tmp/tts.mp3", "wb") as f:
            f.write(speech)

    response = make_response()
    response.data = speech

    response.headers["Content-Disposition"] = "attachment; filename=tts.mp3"
    response.mimetype = "audio/mpeg"

    return response

@main.route("/camera", methods=["GET"])
def capture():
    skip_frames = request.args.get("skip_frames", default=0, type=int)
    rect_image = request.args.get("rect_image", default="false", type=str)
    rect_image = True if rect_image == "true" else False

    b64image = webcam.capture(skip_frames=skip_frames, rect_image=rect_image)
    return (jsonify({"b64image": b64image}))
    
