from face_emotions import find_emotion
from polly_emotions import make_emotion_speech
import subprocess
emotion = find_emotion()
make_emotion_speech(emotion)

subprocess.call(['vlc', 'output.mp3'])
