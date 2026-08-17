# train_model.py
import sys
import os
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from core.evaluator import Evaluator


# ======================================================
# BASE PATH SETUP (IMPORTANT FIX)
# ======================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DATA_PATH = os.path.join(BASE_DIR, "data", "dataset.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

print("Current working dir:", os.getcwd())
print("Dataset path:", DATA_PATH)


# ======================================================
# LOAD DATASET
# ======================================================

df = pd.read_csv(DATA_PATH, header=None)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]


# ======================================================
# TRAIN / TEST SPLIT
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ======================================================
# PCA (DIMENSIONALITY REDUCTION)
# ======================================================

pca = PCA(n_components=10)

X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)


# ======================================================
# CLASSIFIER
# ======================================================

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train_pca, y_train)


# ======================================================
# PREDICTION
# ======================================================

y_pred = model.predict(X_test_pca)


# ======================================================
# EVALUATION
# ======================================================

Evaluator.evaluate(y_test, y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))


# ======================================================
# SAVE MODELS (FIXED PATH)
# ======================================================

joblib.dump(pca, os.path.join(MODEL_DIR, "pca.pkl"))
joblib.dump(model, os.path.join(MODEL_DIR, "classifier.pkl"))

print("Training Complete ✔")