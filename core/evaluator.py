# evaluator.py
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


class Evaluator:

    @staticmethod
    def evaluate(y_true, y_pred):

        print("Accuracy:", accuracy_score(y_true, y_pred))

        print(
            "Precision:",
            precision_score(y_true, y_pred, average='weighted')
        )

        print(
            "Recall:",
            recall_score(y_true, y_pred, average='weighted')
        )

        print(
            "F1 Score:",
            f1_score(y_true, y_pred, average='weighted')
        )

        print("Confusion Matrix:\n")
        print(confusion_matrix(y_true, y_pred))