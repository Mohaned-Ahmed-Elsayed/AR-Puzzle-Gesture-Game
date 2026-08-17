# core/gesture_classifier.py

import joblib
import numpy as np


class GestureClassifier:

    def __init__(
        self,
        model_path="models/classifier.pkl"
    ):

        self.model = joblib.load(model_path)

    def predict(self, features):

        probs = self.model.predict_proba(features)[0]

        max_prob = np.max(probs)

        prediction = self.model.classes_[np.argmax(probs)]

        # =====================================
        # CONFIDENCE FILTER
        # =====================================

        if max_prob < 0.85:
            return "none"

        return prediction