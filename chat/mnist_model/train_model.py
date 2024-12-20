from datasets import load_dataset
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
import numpy as np



# Verifica si TensorFlow está usando la CPU
print("esta usando GPU??????", tf.test.is_gpu_available())
print("########################################\n")
# Cargar el dataset MNIST
ds = load_dataset("ylecun/mnist")

# Obtener los datos de entrenamiento y prueba
x_train, y_train = ds['train']['image'], ds['train']['label']
x_test, y_test = ds['test']['image'], ds['test']['label']

# Función para convertir las imágenes PIL en arrays de NumPy y normalizar
def preprocess_images(images):
    return np.array([np.array(image).astype('float32') / 255.0 for image in images])

# Preprocesar las imágenes
x_train = preprocess_images(x_train)
x_test = preprocess_images(x_test)

# Asegúrate de que las imágenes tengan la forma correcta para el modelo (28, 28, 1)
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# Convertir las etiquetas a formato categórico
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definir el modelo
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))


model.save('mnist_model.keras')
