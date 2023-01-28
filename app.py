import pyttsx3
from flask import Flask, jsonify, make_response, request, send_file
from loguru import logger
import os
import time
from speak import Speak
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/speak/<string:speak_text>", methods = ['POST'])
def speak(speak_text):
    body = request.json
    path_to_file = Speak(speak_text, voice_id = body['voice_id'], rate = body['rate'])
    retry = 3
    while retry >0:
        retry-=1
        if os.path.exists(path_to_file):
            return send_file(
                path_to_file, 
                mimetype="audio/mp3", )
        else:
            time.sleep(15)
            

@app.route("/get_all_voices")
def get_all_voices():
    '''Function to get all voices'''
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        all_voices = []
        for voice in voices:
            voice = voice.__dict__
            voice.pop('languages')
            all_voices.append(voice)
        logger.debug(all_voices)
        response = make_response(jsonify(all_voices))
    except AttributeError as exc:
        raise exc

    return response