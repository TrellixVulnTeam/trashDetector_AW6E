import io
import os
from time import sleep

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
cig_butt = set(['cig'])

not_cig = set(['notcig' ] )


def describe_img(image_url ):
    file_name = os.path.join(os.path.dirname(__file__ ) )
    with io.open(file_name, 'rb' ) import io
    import os
    
    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types
    
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    
    # The name of the image file to annotate
    file_name = os.path.join(
                os.path.dirname(__file__),
                    'resources/wakeupcat.jpg')
    
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            
            image = types.Image(content=content)
            
            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations
            
            print('Labels:')
            for label in labels:
                    print(label.description)as image_file:
        content = image_file.read()



