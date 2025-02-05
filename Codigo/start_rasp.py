import tensorflow as tf
import numpy as np
import cv2
from tensorflow import lite

# Cargar el modelo TensorFlow Lite
interpreter = lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Función para realizar la predicción
def predict_image(image):
    # Preprocesar la imagen (ajustar tamaño y normalizar)
    image_resized = cv2.resize(image, (224, 224))
    image_normalized = np.expand_dims(image_resized, axis=0)
    image_normalized = image_normalized / 255.0  # Normalización

    # Asignar la entrada al modelo
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], image_normalized)
    interpreter.invoke()

    # Obtener el resultado
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data

# Código para capturar una imagen y hacer predicciones
def capture_and_predict():
    # Usar la cámara para capturar la imagen
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if ret:
        prediction = predict_image(frame)
        print("Predicción:", prediction)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_predict()

