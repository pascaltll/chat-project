import random
import tensorflow as tf
import numpy as np
import base64
from io import BytesIO
from PIL import Image
import os
from . image_preproceso import preprocess_image

import json

# Cargar el modelo en formato .keras
model = tf.keras.models.load_model('chat/mnist_model/mnist_model.keras')  

def recognize_number(image_data):
    
    if image_data.startswith('data:image'):
            image_data = image_data.split(',')[1]

    image_bytes = base64.b64decode(image_data)
        
    image_path = 'chat/mnist_model/number.png'
    #image_path = uploaded_image.png
    with open(image_path, 'wb') as img_file:
        img_file.write(image_bytes)


    image = preprocess_image(image_path=image_path)
    prediction = model.predict(image)
    recognized_number = np.argmax(prediction)
    print(f'numero reconocido {recognize_number}')
    return recognized_number