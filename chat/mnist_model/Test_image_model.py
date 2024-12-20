import tensorflow as tf
import numpy as np
from PIL import Image

import json
model = tf.keras.models.load_model('chat/mnist_model/mnist_model.keras')  

def preprocess_image(image_path):
    # Cargar la imagen
    #image = Image.open(image_path).convert('L')  # Convertir a escala de grises (L)
    
    # Redimensionar la imagen a 28x28 píxeles
    image = Image.open(image_path).convert('RGBA')
    background = Image.new('RGBA', image.size, (255, 255, 255, 255))  # Fondo blanco
    background.paste(image, (0, 0), image)
    image = background.convert('L')
    image = Image.eval(image, lambda x: 255 - x)

    image = image.resize((28, 28))

    # Convertir la imagen a un arreglo numpy y normalizar los valores de píxeles
    image = np.array(image).astype('float32') / 255.0  # Normalizar

    # Redimensionar para que sea compatible con el modelo (batch_size, height, width, channels)
    image = image.reshape(1, 28, 28, 1)
    
    return image

def recognize_number_from_image(image_path):
    # Preprocesar la imagen
    image = preprocess_image(image_path)
    
    # Hacer la predicción con el modelo
    prediction = model.predict(image)
    
    # Obtener el número con la mayor probabilidad
    recognized_number = np.argmax(prediction)
    
    return recognized_number

image_path = 'uploaded_image.png'
image_path = 'chat/mnist_model/number.png'

recognized_number = recognize_number_from_image(image_path)

# Imprimir el número reconocido
print(f"El número reconocido es: {recognized_number}")