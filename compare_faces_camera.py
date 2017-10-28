import requests
from pprint import pprint
import boto3
import subprocess
import json

s3 = boto3.client('s3')

filename1 = "pics/image1.jpeg"
pathname1 = 'image1.jpeg'
filename2 = "pics/image2.jpeg"
pathname2 = 'image2.jpeg'
bucket_name = 'hackathon2017bucket'

subprocess.call(["streamer", "-f", "jpeg", "-o", pathname1])
subprocess.call(["streamer", "-f", "jpeg", "-o", pathname2])

s3.upload_file(pathname1, bucket_name, filename1)
s3.upload_file(pathname1, bucket_name, filename2)

subprocess.call(["rm", pathname1])
subprocess.call(["rm", pathname2])

client = boto3.client('rekognition')

response=client.compare_faces(SimilarityThreshold=70,
                              SourceImage={'S3Object':{'Bucket':bucket_name,'Name':filename1}},
                              TargetImage={'S3Object':{'Bucket':bucket_name,'Name':filename2}})

for faceMatch in response['FaceMatches']:
    position = faceMatch['Face']['BoundingBox']
    confidence = str(faceMatch['Face']['Confidence'])
    print('The face at ' +
           str(position['Left']) + ' ' +
           str(position['Top']) +
           ' matches with ' + confidence + '% confidence')
