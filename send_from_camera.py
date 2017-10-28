import requests
from pprint import pprint
import boto3
import subprocess

s3 = boto3.client('s3')

filename = "pics/image.jpeg"
pathname = 'image.jpeg'
bucket_name = 'hackathon2017bucket'

subprocess.call(["streamer", "-f", "jpeg", "-o", pathname])

s3.upload_file(pathname, bucket_name, filename)

subprocess.call(["rm", pathname])

client = boto3.client('rekognition')

response = client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':filename}},MinConfidence=75)

human_list = ["Human", "People", "Person", "Selfie"]

print('Detected labels for ' + filename)
for label in response['Labels']:
    if label['Name'] not in human_list:
        print (label['Name'] + ' : ' + str(label['Confidence']))
