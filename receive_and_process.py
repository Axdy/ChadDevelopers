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

client = boto3.client('rekognition') #initialize recognition API
s3 = boto3.resource('s3') #initialize s3 bucket API
filename = 'banana.jpg' #name of file saved on S3
bucket_name = 'hackathon2017bucket' #bucket name
s3.Bucket(bucket_name).download_file(filename, 'pics/downloaded.jpg') #download image from the Bucket.

imgbytes = get_image_from_file('pics/downloaded.jpg') #read in the downloaded image

c = client.detect_labels(Image={'Bytes': imgbytes}) #process image and find labels

for label in c['Labels']: #get labels from the output from API
    print label
