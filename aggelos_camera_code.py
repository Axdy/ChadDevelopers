import requests
from pprint import pprint
import boto3
import subprocess

def get_image_url(imgurl):
    resp = requests.get(imgurl)
    return resp.content

def get_image_from_file(filename):
    with open(filename, 'rb') as img:
        return img.read()

client = boto3.client('rekognition')

filename = "image.jpeg"

subprocess.call(["streamer", "-f", "jpeg", "-o", filename])

#url = "http://www.ciaoimports.com/assets/images/Banana.jpg"

#imgbytes = get_image_url(url)
imgbytes = get_image_from_file(filename)

c = client.detect_labels(Image={'Bytes': imgbytes})

#pprint(c)

for label in c['Labels']:
    print label
