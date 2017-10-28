#Creates an mp3 file of the text inserted and returns it
import boto3
import os

polly = boto3.client('polly')
spoken_text = polly.synthesize_speech(Text= 'Hey! You look happy. Here is a playlist for your moods.', OutputFormat= 'mp3', VoiceId = 'Joanna')

with open('output.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()
