from files.data import get_data
from files.evaluation import evaluate
from models.train import train_all
from models.tune import grid_search

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def print_metrics(name, metrics):
    print(f"\n{name}")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

# Load data
X_train, X_test, y_train, y_test = get_data()

# Train base models
models = train_all(X_train, y_train)

# Evaluate base models
print("Base Model Evaluation:")
for name, model in models.items():
    scores = evaluate(model, X_test, y_test)
    print_metrics(name, scores)

# Tune RandomForest
rf_params = {
    'n_estimators': [100, 150],
    'max_depth': [None, 5, 10]
}
best_rf, rf_best_params = grid_search(RandomForestClassifier(), rf_params, X_train, y_train)
print("\nTuned Random Forest Parameters:", rf_best_params)
print_metrics("Tuned RandomForest", evaluate(best_rf, X_test, y_test))

# Tune SVM
svm_params = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}
best_svm, svm_best_params = grid_search(SVC(), svm_params, X_train, y_train)
print("\nTuned SVM Parameters:", svm_best_params)
print_metrics("Tuned SVM", evaluate(best_svm, X_test, y_test))
