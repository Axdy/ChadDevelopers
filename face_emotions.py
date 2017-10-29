# Returns the three most dominant emotions identified on the picture take from the webcam
# Prints a sorted dictionary where the keys are the percentages and the elements are the emotions
import requests
from pprint import pprint
import boto3
import subprocess
import json
import collections

def make_name(i):
    name_core = "image0"
    name_end = ".jpeg"
    return name_core + str(i) + name_end

def find_emotion():
    s3 = boto3.client('s3')

    filename = "pics/image.jpeg"
    pathname = 'image00.jpeg'
    bucket_name = 'hackathon2017bucket'
    num_of_frames = 5
    read_name = make_name(num_of_frames-1)
    subprocess.call(["streamer", "-t", str(num_of_frames), "-r", "1", "-f", "jpeg", "-o", pathname])
    for i in range(num_of_frames-1):
        subprocess.call(["rm", make_name(i)])
    s3.upload_file(read_name, bucket_name, filename)

    client = boto3.client('rekognition')
    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket_name,'Name':filename}}, Attributes=['ALL'])
    emotions = []
    for faceDetail in response['FaceDetails']:
        output = (json.dumps(faceDetail['Emotions'], sort_keys=True))
        for emotion in faceDetail['Emotions'][:]:
            emotions.append(emotion)
    max_emotion = emotions[0]
    for emotion in emotions:
        if int(emotion["Confidence"]) > int(max_emotion["Confidence"]):
            max_emotion = emotion
    final_emotion = str(max_emotion["Type"])
    if final_emotion not in ["HAPPY", "ANGRY", "SAD", "CONFUSED"]:
        final_emotion = "DEFAULT"
    print "\n" + final_emotion
    return final_emotion

#print "\n" + find_emotion()
