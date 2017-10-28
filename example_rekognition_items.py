import boto3  
import json

rek = boto3.client('rekognition') # Setup the Rekognition Client  
s3 = boto3.resource('s3') # Setup the S3 Resource

print "Getting Image"  
image = s3.Object('my-amazing-bucket', 'picnic.png') # Get an image to work with  
img_data = image.get()['Body'].read() # Read the image

print "Image retrieved"  
print "Sending to Rekognition"

# Detect the items in the image
results = rek.detect_labels(  
            Image={
                'Bytes': img_data }
            )

print "Rekognition done"

# Print the result
print json.dumps(  
            results['Labels'],
                indent=2
                )

# Print a message for each item
for label in results["Labels"]:  
        print "I am {}% confident of of the image having a {} in it".format(
                        int(label['Confidence']),
                                label['Name'],
                                    )
