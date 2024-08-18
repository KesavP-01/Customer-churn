import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


def preprocessing(filepath):

    df = pd.read_csv(filepath)
    X = df.iloc[:, 3:-1].values
    y = df.iloc[:, -1].values

    encoder = LabelEncoder()
    X[:, 2] = encoder.fit_transform(X[:, 2])

    transformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
    X = np.array(transformer.fit_transform(X))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    return X_train, X_test, y_train, y_test


