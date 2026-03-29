from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def get_models():
    """
    Returns dictionary of models.
    """

    models = {

        "Naive Bayes": MultinomialNB(),

        "Random Forest": RandomForestClassifier(),

        "SVM": SVC(probability=True)

    }

    return models
