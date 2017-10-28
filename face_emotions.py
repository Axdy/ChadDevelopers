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
    pathname = 'image00.jpeg'
    bucket_name = 'hackathon2017bucket'
    read_name = "image02.jpeg" 
    subprocess.call(["streamer", "-t", "3", "-r", "1", "-f", "jpeg", "-o", pathname])

    s3.upload_file(read_name, bucket_name, filename)
    #subprocess.call(["rm", pathname])

    client = boto3.client('rekognition')
    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket_name,'Name':filename}}, Attributes=['ALL'])
    print "PRE EMOITIONS 0."
    print response
    emotions = []
    for faceDetail in response['FaceDetails']:
        output = (json.dumps(faceDetail['Emotions'], sort_keys=True))
        print "DUMPS CHECK 1.\n"
        print output
        for emotion in faceDetail['Emotions'][:]:
            print "EMOTION CHECK 2."
            emotions.append(emotion)
    print "ARRAY CHECK 3.\n"
    max_emotion = emotions[0]
    for emotion in emotions:
        if int(emotion["Confidence"]) > int(max_emotion["Confidence"]):
            max_emotion = emotion
    final_emotion = str(max_emotion["Type"])
    if final_emotion not in ["HAPPY", "ANGRY", "SAD", "CONFUSED"]:
        final_emotion = "DEFAULT"
    return final_emotion

#print "\n" + find_emotion()
