from flask import Flask, flash, redirect, render_template, request, session, abort
import hello
from face_emotions import find_emotion
from polly_emotions import make_emotion_speech
from find_playlist import find_emotion_playlist
import subprocess
import time
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('layout.html')



@app.route('/generate')
def generate(name=None):
    #hello.main()
    emotion = find_emotion()
    make_emotion_speech(emotion)

    vlc = subprocess.Popen(['cvlc', 'output.mp3'])
    time.sleep(5)
    vlc.kill()
    find_emotion_playlist(emotion)
    return render_template('process.html',name=name)

if __name__ == "__main__":
    app.run()
