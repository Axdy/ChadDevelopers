import boto3

s3 = boto3.client('s3')
s3down = boto3.resource('s3')

pathname = 'banana1.jpg'
bucket_name = 'hackathon2017bucket'
filename = 'pics/banana1.jpg'
s3.upload_file(filename, bucket_name, pathname)

#Download the image from bucket.
s3down.Bucket(bucket_name).download_file(pathname, 'pics/downloadede.jpg')

