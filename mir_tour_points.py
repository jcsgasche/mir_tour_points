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
    
def run_flask_video(video, sound, delay):
    time.sleep(delay)
    flask_video(video, sound)
        


class MirTourPoints():
    def __init__(self):
        global tts
        global fsio
        self.mir_tour_infos = mir_tour_infos
        flask()
        #image_thread = Thread(target= run_flask_image, args=())

    def p1(cls):
        threads = []

        # Start threads and add them to the list
        tts_thread = Thread(target=run_tts, args=("1",))
        tts_thread.start()
        threads.append(tts_thread)
        
        image_thread1 = Thread(target=run_flask_image, args=('p1/tim_berners_lee.jpg', 10, 2))
        image_thread1.start()
        threads.append(image_thread1)
        
        image_thread2 = Thread(target=run_flask_image, args=('p1/ml.jpg', 5, 25))
        image_thread2.start()
        threads.append(image_thread2)
        
        image_thread3 = Thread(target=run_flask_image, args=('p1/robots.png', 5, 40))
        image_thread3.start()
        threads.append(image_thread3)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    def p2(cls):
        threads = []
        
        tts_thread = Thread(target=run_tts, args=("2",))
        tts_thread.start()
        threads.append(tts_thread)
        
        video_thread = Thread(target=run_flask_video, args=('p2/irc.mp4', False, 2))
        video_thread.start()
        threads.append(video_thread)
        
        image_thread1 = Thread(target=run_flask_image, args=('p2/grace_hopper.png', 2, 35))
        image_thread1.start()
        threads.append(image_thread1)
        
        image_thread2 = Thread(target=run_flask_image, args=('p2/real_admiral_grace_hopper.jpg', 3, 37))
        image_thread2.start()
        threads.append(image_thread2)
        
        image_thread3 = Thread(target=run_flask_image, args=('p2/compiler.jpg', 5, 42))
        image_thread3.start()
        threads.append(image_thread3)
        
        image_thread4 = Thread(target=run_flask_image, args=('p2/cobol.jpeg', 5, 50))
        image_thread4.start()
        threads.append(image_thread4)
        
        for thread in threads:
            thread.join()
            
    def p3(cls):
        threads = []
        
        tts_thread = Thread(target=run_tts, args=("3",))
        tts_thread.start()
        threads.append(tts_thread)
        
        image_thread1 = Thread(target=run_flask_image, args=('p3/alan_turing.jpg', 3, 2))
        image_thread1.start()
        threads.append(image_thread1)
        
        image_thread2 = Thread(target=run_flask_image, args=('p3/alan_turing_2.jpg', 3, 6))
        image_thread2.start()
        threads.append(image_thread2)
        
        image_thread3 = Thread(target=run_flask_image, args=('p3/turing_test.jpg', 5, 12))
        image_thread3.start()
        threads.append(image_thread3)
        
        image_thread4 = Thread(target=run_flask_image, args=('p3/ww2.jpg', 5, 20))
        image_thread4.start()
        threads.append(image_thread4)
            
        for thread in threads:
            thread.join()
    
    def p4(cls):
        threads = []
        
        tts_thread = Thread(target=run_tts, args=("4",))
        tts_thread.start()
        threads.append(tts_thread)
        
        image_thread1 = Thread(target=run_flask_image, args=('p4/peppers.jpg', 7, 5))
        image_thread1.start()
        
        image_thread2 = Thread(target=run_flask_image, args=('p4/conversation.jpg', 10, 16))
        image_thread2.start()
        
        for thread in threads:
            thread.join()
            
    def p7(cls):
        threads = []
        
        tts_thread = Thread(target=run_tts, args=("7",))
        tts_thread.start()
        threads.append(tts_thread)
        
        image_thread1 = Thread(target=run_flask_image, args=('p7/konrad_zuse.jpg', 5, 3))
        image_thread1.start()
        threads.append(image_thread1)
        
        image_thread2 = Thread(target=run_flask_image, args=('p7/z3.jpg', 5, 10))
        image_thread2.start()
        threads.append(image_thread2)
        
        image_thread3 = Thread(target=run_flask_image, args=('p7/plankalkuel.png', 5, 20))
        image_thread3.start()
        threads.append(image_thread3)
        
        for thread in threads:
            thread.join()
            
    def p16(cls):
        threads = []
        
        tts_thread = Thread(target=run_tts, args=("16",))
        tts_thread.start()
        threads.append(tts_thread)
        
        image_thread1 = Thread(target=run_flask_image, args=("p16/mir.jpg", 5, 5))
        image_thread1.start()
        threads.append(image_thread1) 
        
        image_thread2 = Thread(target=run_flask_image, args=("p16/team.jpg", 5, 15))
        image_thread2.start()
        threads.append(image_thread2)
        
        video_thread1 = Thread(target=run_flask_video, args=("p16/go1.mp4", False, 52))
        video_thread1.start()
        threads.append(video_thread1)
        
        video_thread2 = Thread(target=run_flask_video, args=("p16/go1_exploration.mp4", False, 60))
        video_thread2.start()
        threads.append(video_thread2)
        
        image_thread3 = Thread(target=run_flask_image, args=("p16/spot.jpg", 5, 73))
        image_thread3.start()
        threads.append(image_thread3)
    
        video_thread3 = Thread(target=run_flask_video, args=("p16/dance.mp4", False, 80))
        video_thread3.start()
        threads.append(video_thread3)
        
        video_thread4 = Thread(target=run_flask_video, args=("p16/spot_action.mp4", False, 90))
        video_thread4.start()
        threads.append(video_thread4)
        
        image_thread4 = Thread(target=run_flask_image, args=("p16/peppers.jpg", 5, 104))
        image_thread4.start()
        threads.append(image_thread4)
        
        image_thread5 = Thread(target=run_flask_image, args=("p16/qt.png", 5, 110))
        image_thread5.start()
        threads.append(image_thread5)
        
        video_thread5 = Thread(target=run_flask_video, args=("p16/packbot.mp4", False, 118))
        video_thread5.start()
        threads.append(video_thread5)
                
        for thread in threads:
            thread.join()
            
    def p18(cls):
        threads = []

        tts_thread = Thread(target=run_tts, args=("18",))
        tts_thread.start()
        threads.append(tts_thread)
        
        image_thread1 = Thread(target=run_flask_image, args=("p18/margaret_hamilton.jpg", 4, 15))
        image_thread1.start()
        threads.append(image_thread1)
        
        image_thread2 = Thread(target=run_flask_image, args=("p18/steve_wozniak.jpg", 4, 20))
        image_thread2.start()
        threads.append(image_thread2)
        
        for thread in threads:
            thread.join()
        
    def p99(cls):
        run_tts("99")
            
if __name__ == "__main__":
    pass