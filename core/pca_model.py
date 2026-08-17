# pca_model.py
import joblib


class PCATransformer:

    def __init__(self, model_path="models/pca.pkl"):
        self.pca = joblib.load(model_path)

    def transform(self, features):
        return self.pca.transform(features)