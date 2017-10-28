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
