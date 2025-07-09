from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def train_all(X_train, y_train):
    models = {
        'LogisticRegression': LogisticRegression(),
        'RandomForest': RandomForestClassifier(),
        'SVM': SVC()
    }

    for name in models:
        models[name].fit(X_train, y_train)
    
    return models
