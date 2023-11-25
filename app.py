

import os
import json
import requests
import time
from flask import Flask, request, jsonify
from inference import model_loading, bangla_tts


DEBUG = True
tts_model = model_loading()

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def process_text():
    st = time.time()
    data = request.get_json()
    sender = data.get('sender', '')
    text = data.get('text', '')
    save_dir = data.get("save_dir", )
    print("==============================")
    print("request : ", request)
    print("==============================")
    print(f"sender : {sender}")
    print(f"text : {text}")

    audio= bangla_tts(
        model= tts_model, 
        text = text, 
        is_male = False, 
        is_e2e_vits = True,
        log_dir = save_dir
     )

    print("type : ", type(audio))
    response = {
        "audio_url"     : audio,
        "sender"    : sender,
        "status"    : 200,
        "processing_time" : time.time()-st
    }


    return response


if __name__ == '__main__':
    app.run(debug=True, host="192.168.0.114",port=8009)