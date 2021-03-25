from tensorflow.keras.models import load_model
import numpy as np

class Gesture:
    def __init__(self):
        self.model = load_model("RPS.h5")
    def predict(self,image):
        image = np.asarray(image,dtype=np.float32)
        image = image[np.newaxis,...]
        image = image/255.0
        return self.model.predict_classes(image)[0],np.max(self.model.predict(image))