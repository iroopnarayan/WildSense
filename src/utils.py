import cv2
import numpy as np
from tensorflow.keras.models import load_model

def load_best_model(model_path):
    return load_model(model_path)

def predict_image(model, image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64))
    img = np.expand_dims(img, axis=0) / 255.0
    prediction = model.predict(img)
    return np.argmax(prediction)

def detect_live(model):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        img = cv2.resize(frame, (64, 64))
        img = np.expand_dims(img, axis=0) / 255.0
        prediction = model.predict(img)
        species = np.argmax(prediction)  # Map this to your class names
        cv2.putText(frame, f'Species: {species}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Animal Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
