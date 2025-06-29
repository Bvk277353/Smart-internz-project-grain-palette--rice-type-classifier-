import tensorflow as tf
import numpy as np
from PIL import Image

interpreter = tf.lite.Interpreter(model_path="rice_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

with open("labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

def classify_rice(image_path):
    img = Image.open(image_path).convert("RGB").resize((224, 224))
    img = np.array(img, dtype=np.float32)
    img = (img - 127.5) / 127.5
    img = np.expand_dims(img, axis=0)

    interpreter.set_tensor(input_details[0]["index"], img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]["index"])[0]

    top_index = np.argmax(output)
    confidence = float(output[top_index])
    label = labels[top_index]

    return label, round(confidence * 100, 2)