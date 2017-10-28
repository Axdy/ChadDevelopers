from face_emotions import find_emotion
from polly_emotions import make_emotion_speech
from find_playlist import find_emotion_playlist
import subprocess
import time
emotion = find_emotion()
make_emotion_speech(emotion)
'''
vlc = subprocess.Popen(['vlc', 'output.mp3'], shell=True)
time.sleep(10)
vlc.kill()'''
find_emotion_playlist(emotion)
