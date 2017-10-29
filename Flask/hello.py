import boto3
import os
from playsound import playsound

def main():
    polly = boto3.client('polly')
    spoken_text = polly.synthesize_speech(Text= 'Hey! You look happy. Here is a playlist for your moods.', OutputFormat= 'mp3', VoiceId = 'Joanna')

    with open('output.mp3', 'wb') as f:
        f.write(spoken_text['AudioStream'].read())
        f.close()
    
#playsound('output.mp3')

