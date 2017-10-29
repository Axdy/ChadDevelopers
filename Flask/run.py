from face_emotions import find_emotion
from polly_emotions import make_emotion_speech
from find_playlist import find_emotion_playlist
import subprocess
import time

def run():
    emotion = find_emotion()
    make_emotion_speech(emotion)

    #vlc = subprocess.Popen(['cvlc', 'output.mp3'])
    time.sleep(2)
    #vlc.kill()
    find_emotion_playlist(emotion)
