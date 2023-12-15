import sys
import os
import json
import time
from threading import Thread

ak = os.path.expanduser("~/mir_tour/api-keys")
gb = os.path.expanduser("~/mir_tour/gpt-bot")
fa = os.path.expanduser("~/mir_tour/flask-avatar")

paths = [ak, gb, fa]
for path in paths:
    sys.path.append(path)
    
from flask_socket import FlaskSocketIO
fsio = FlaskSocketIO()

    
mir_tour_infos_path = os.path.expanduser("~/mir_tour/mir_tour_infos/mir_tour.json")

with open(mir_tour_infos_path, 'r') as f:
    mir_tour_infos = json.load(f)


from api_keys import (AZURE_SPEECH_KEY)

from helpers.tts import AzureTTS

AZURE_SPEECH_REGION = "switzerlandnorth"
model_name = 'de-DE-ConradNeural'
#model_name = 'de-CH-JanNeural'
#model_name = 'de-CH-LeniNeural'

tts = AzureTTS(
    api_key=AZURE_SPEECH_KEY, 
    region=AZURE_SPEECH_REGION, 
    model_name=model_name, 
    play=True)

def run_tts(point):
    tts.tts(mir_tour_infos[point])


def flask():
    global fsio
    thread = Thread(target=lambda: fsio.socketio.run(fsio.app))
    thread.start()
    
def flask_image(image, duration):
    global fsio
    url = f'http://127.0.0.1:5000/static/images/{image}'
    content_info = {
        'type': 'image',
        'url': url,
        'duration': duration
    }
    fsio.socketio.emit('show_content', content_info)
    
def run_flask_image(image, duration, delay):
    time.sleep(delay)
    flask_image(image, duration)
    
def flask_video(video, sound):
    global fsio
    url = f'http://127.0.0.1:5000/static/videos/{video}'
    content_info = {
        'type': 'video',
        'url': url,
        'sound': sound
    }
    fsio.socketio.emit('show_content', content_info)


class MirTourPoints:
    def __init__(self):
        global tts
        global fsio
        self.mir_tour_infos = mir_tour_infos
        flask()

    def p1(cls):
        tts_thread = Thread(target=run_tts, args=("1"))
        tts_thread.start()
        
        image_thread = Thread(target= run_flask_image, args=('tim_berners_lee.jpg',7,5))
        image_thread.start()

    def p2(cls):
        tts.tts(mir_tour_infos["2"])
        
        
if __name__ == "__main__":
    tts.tts("Let's go")