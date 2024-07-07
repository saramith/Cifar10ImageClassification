import numpy as np
from tensorflow.keras.models import load_model
from src.data_ingestion import load_cifar10_data
from src.data_preprocessing import preprocess_data

def evaluate_model():
    model = load_model("trained_model.h5")
    
    (_, _), (X_test, y_test) = load_cifar10_data()
    _, X_test, _, y_test = preprocess_data(np.empty((0, 32, 32, 3)), X_test, np.empty((0, 1)), y_test)
    
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=1)

    return {
        'test_loss': test_loss,
        'test_accuracy': test_acc
    }
