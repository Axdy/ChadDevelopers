# Returns the three most dominant emotions identified on the picture take from the webcam
# Prints a sorted dictionary where the keys are the percentages and the elements are the emotions
import requests
from pprint import pprint
import boto3
import subprocess
import json
import collections

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
        first_emotion = str(faceDetail['Emotions'][:][0]["Type"])
        second_emotion = str(faceDetail['Emotions'][:][1]["Type"])
        third_emotion = str(faceDetail['Emotions'][:][2]['Type'])

        first_emotion_val = str(faceDetail['Emotions'][:][0]["Confidence"])
        second_emotion_val = str(faceDetail['Emotions'][:][1]["Confidence"])
        third_emotion_val = str(faceDetail['Emotions'][:][2]["Confidence"])

emotions = {}
emotions[first_emotion] = first_emotion_val
emotions[second_emotion] = second_emotion_val
emotions[third_emotion] = third_emotion_val

emotions_dict = collections.OrderedDict(sorted(emotions.items()))

print emotions_dict
