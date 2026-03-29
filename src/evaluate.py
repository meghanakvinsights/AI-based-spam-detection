from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance.
    """

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    report = classification_report(y_test, predictions)

    return accuracy, report
