import joblib as jl
from sklearn.metrics import accuracy_score, roc_auc_score
from scripts.python.preprocessing import preprocessing

def modelScores(filepath, datapath):

    X_train, X_test, y_train, y_test = preprocessing(datapath)

    model = jl.load(filepath)

    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5)

    accuracy = accuracy_score(y_test, y_pred)
    rocScore = roc_auc_score(y_test, y_pred)

    return accuracy, rocScore

if __name__ == "__main__":

    accuracy, rocScore = modelScores('models/churnModel', 'data/Churn.csv')

    print(f'Accuracy of the Model is {accuracy} and ROC value is {rocScore}')


