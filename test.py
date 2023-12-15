import sys
import os
import json

ak = os.path.expanduser("~/mir_tour/api-keys")
gb = os.path.expanduser("~/mir_tour/gpt-bot")

paths = [ak, gb]
for path in paths:
    sys.path.append(path)
    
mir_tour_infos_path = os.path.expanduser("~/mir_tour/mir_tour_infos/mir_tour.json")

with open(mir_tour_infos_path, 'r') as f:
    mir_tour_infos = json.load(f)

from api_keys import (AZURE_SPEECH_KEY)

from helpers.stt import AzureSTT
from helpers.tts import AzureTTS

def speech():
    global stt
    global tts

    AZURE_SPEECH_REGION = "switzerlandnorth"
    model_name = 'de-DE-ConradNeural'
    #model_name = 'de-CH-JanNeural'
    #model_name = 'de-CH-LeniNeural'

    stt = AzureSTT(
        api_key=AZURE_SPEECH_KEY, 
        region=AZURE_SPEECH_REGION, 
        language='de-DE', verbose=True, 
        conversation_timeout=20)

    tts = AzureTTS(
        api_key=AZURE_SPEECH_KEY, 
        region=AZURE_SPEECH_REGION, 
        model_name=model_name, 
        play=True)

def main():
    speech()
    global tts
    tts.tts(
        mir_tour_infos["1"]
    )

"""
1: 

5 Tim Berners-Lee
12 WWW
15 Roboter
38 ML
1:00 Tim Berners-Lee

2:
"""


if __name__ == "__main__":
    main()