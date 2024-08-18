from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense, Activation
from keras._tf_keras.keras.optimizers import Adam
from keras._tf_keras.keras.metrics import binary_crossentropy
from scripts.python.preprocessing import preprocessing
import joblib

def churnModel(filepath):

    X_train, X_test, y_train, y_test = preprocessing(filepath)

    model = Sequential([
        Dense(16, activation='relu'),
        Dense(32, activation="relu"),
        Dense(1, activation="sigmoid")
    ])

    model.compile(optimizer=Adam(learning_rate=0.0001), loss=binary_crossentropy, metrics=['accuracy'])
    model.fit(X_train, y_train, validation_split=0.1, batch_size=32, epochs=100, shuffle=True, verbose=2)

    return model