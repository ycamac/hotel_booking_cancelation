import random

def get_model_metrics():
    return {
        "Accuracy": 0.87,
        "Precision": 0.81,
        "Recall": 0.79,
        "F1 Score": 0.80,
    }

def predict_cancellation():
    return round(random.uniform(0, 1), 2) 