#Creates an mp3 file of the text inserted and returns it
import boto3
import os

def make_emotion_speech(emotion):
    polly = boto3.client('polly')
    if emotion == "DEFAULT":
        text = "Hey! I don't know what you're feeling, but here's a playlist anyway."
    else:
        text = "Hey! You look " + emotion + ". Here is a playlist for your mood."
    spoken_text = polly.synthesize_speech(Text= text, OutputFormat= 'mp3', VoiceId = 'Joanna')

    with open('output.mp3', 'wb') as f:
        f.write(spoken_text['AudioStream'].read())
        f.close()
