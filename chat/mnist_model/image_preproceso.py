import numpy as np
from PIL import Image


def preprocess_image(image_path):
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