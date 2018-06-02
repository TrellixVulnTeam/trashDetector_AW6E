import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
# Instantiates a client
client = vision.ImageAnnotatorClient()
valid_items = set(['bottle ', 'cigarette', 'plsatic bag'  ])
file_name = os.path.join(
            os.path.dirname(__file__),
                '/home/null/Workspace/bottle.jpg')
# Loads the image into memory

def giveDescription(image_url ):
    file_name = os.path.join(os.path.dirname(__file__), image_url)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content ) 
    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        print(label.description )
        if(label.description == " cigarette" ):
            print("is trash")
            break
        else:
            print ("is not trash")


giveDescription('/home/null/Workspace/recog/nekochan.jpg' )

# with io.open(file_name, 'rb') as image_file:
#        content = image_file.read()

#        image = types.Image(content=content)

#        # Performs label detection on the image file
#        response = client.label_detection(image=image)
#        labels = response.label_annotations 
      #  print('Labels:')
       # for label in labels:
        #        print(label.description)
         #       if label.description =='cigerette':
          #          print("is a cig")
           #     else:
            #        print("not a cig")
                
