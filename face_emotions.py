# Returns the three most dominant emotions identified on the picture take from the webcam
# Prints a sorted dictionary where the keys are the percentages and the elements are the emotions
import requests
from pprint import pprint
import boto3
import subprocess
import json
import collections

def find_emotion():
    s3 = boto3.client('s3')

    filename = "pics/image.jpeg"
    pathname = 'image.jpeg'
    bucket_name = 'hackathon2017bucket'

    subprocess.call(["streamer", "-f", "jpeg", "-o", pathname])

    s3.upload_file(pathname, bucket_name, filename)
    subprocess.call(["rm", pathname])

    client = boto3.client('rekognition')
    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket_name,'Name':filename}}, Attributes=['ALL'])

    for faceDetail in response['FaceDetails']:
        print('Here are the emotion attributes detected:')

        output = (json.dumps(faceDetail['Emotions'], sort_keys=True))
    	emotions = []
    	for emotion in faceDetail['Emotions'][:]:
            emotions.append(emotion)

    if emotions:
    	max_emotion = emotions[0]
    	for emotion in emotions:
    		if int(emotion["Confidence"]) > int(max_emotion["Confidence"]):
    			max_emotion = emotion
    else:
    	max_emotion = None
    final_emotion = str(max_emotion["Type"])
    if final_emotion not in ["HAPPY", "ANGRY", "SAD", "SUPRISED", "CONFUSED"]:
        final_emotion = None
    return final_emotion

print find_emotion()
