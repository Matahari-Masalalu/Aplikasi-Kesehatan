import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf

class SkinDiseaseClassifier:
    def __init__(self, model_path, label_path):
        self.interpreter = self.load_model(model_path)
        self.class_names = self.load_labels(label_path)

    def load_labels(self, label_path):
        with open(label_path, 'r') as file:
            return [line.strip().split(' ', 1)[1] for line in file.readlines()]

    def load_model(self, model_path):
        interpreter = tf.lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()
        return interpreter

    def classify_image(self, image, img_size=(450, 450)):
        image = ImageOps.fit(image, img_size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image) / 255.0
        data = np.expand_dims(image_array, axis=0).astype(np.float32)

        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

        self.interpreter.set_tensor(input_details[0]['index'], data)
        self.interpreter.invoke()

        prediction = self.interpreter.get_tensor(output_details[0]['index'])
        top_prob_index = np.argmax(prediction[0])
        confidence_score = float(prediction[0][top_prob_index])
        return self.class_names[top_prob_index], confidence_score