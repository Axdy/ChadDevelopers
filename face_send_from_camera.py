import requests
from pprint import pprint
import boto3
import subprocess
import json

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
    print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
    print('Here are the other attributes:')
    print(json.dumps(faceDetail, indent=4, sort_keys=True))
