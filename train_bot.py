from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import pandas as pd
import joblib
def old_stupid_bot():

    DATA_FILE = 'generated_data.csv'

    FEATURES = [
        'p_x',
        'e_x',
        'e_y',
        'dist_x',
        'dist_y'
    ]

    TARGET = 'action'

    def load_data():
        df = pd.read_csv(DATA_FILE)

        print("==================== \nInfo: \n")
        print(df.info())

        print("==================== \nFirst columns: \n")
        print(df.head())

        return df

    def prep_data(df):
        req_cols = FEATURES + [TARGET]
        df = df[req_cols].copy()

        df = df.dropna()
        X = df[FEATURES]
        y =df[TARGET]

        return X, y

    def split_data(X, y):
        return train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

    def train_model(X_train, y_train):
        model = DecisionTreeClassifier(
            max_depth=6, 
            class_weight="balanced",
            random_state=42
        )

        model.fit(X_train, y_train)

        return model

    def evaluate_model(model, X_train, X_test, y_train, y_test):
        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        train_accuracy = model.score(X_train, y_train)
        print(f"Train accuracy: {train_accuracy}")
        print(f"Test accuracy: {round(accuracy, 2)}")

    def save_model(model):
        model_data = {
            'model': model,
            'feature_columns': FEATURES
        }

        joblib.dump(model_data, "my_model.joblib")

        print("\nModel successfully saved")


    df = load_data()
    X, y = prep_data(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    model = train_model(X_train, y_train)

    evaluate_model(model, X_train, X_test, y_train, y_test)
    save_model(model)

def new_smart_fella():
    
    DATA_FILE = 'game_data2.csv'

    FEATURES = ['p_x',
                'e_x0',
                'e_y0',
                'dist_x0',
                'dist_y0',
                'e_x1',
                'e_y1',
                'dist_x1',
                'dist_y1',
                'e_x2',
                'e_y2',
                'dist_x2',
                'dist_y2',
                'e_x3',
                'e_y3',
                'dist_x3',
                'dist_y3',
                'e_x4',
                'e_y4',
                'dist_x4',
                'dist_y4'
                ]
    
    TARGET = 'action'

    def load_data():
        df = pd.read_csv(DATA_FILE)
    
        print("==================== \nInfo: \n")
        print(df.info())
    
        print("==================== \nFirst columns: \n")
        print(df.head())

        
        print("==================== \nAction count: \n")
        print(df.groupby('action').size())
    
        return df

    def prep_data(df):
        req_cols = FEATURES + [TARGET]
        df = df[req_cols].copy()

        df = df.dropna()
        X = df[FEATURES]
        y = df[TARGET]

        print(X.info())
        print(y.info())

        return X, y

    def split_data(X, y):
        return train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

    def train_model(X_train, y_train):
        model = DecisionTreeClassifier(
            max_depth=6, 
            class_weight="balanced",
            random_state=42
        )

        model.fit(X_train, y_train)

        return model

    def evaluate_model(model, X_train, X_test, y_train, y_test):
        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        train_accuracy = model.score(X_train, y_train)
        print(f"Train accuracy: {train_accuracy}")
        print(f"Test accuracy: {round(accuracy, 2)}")

    def save_model(model):
        model_data = {
            'model': model,
            'feature_columns': FEATURES
        }

        joblib.dump(model_data, "my_smartpants.joblib")

        print("\nModel successfully saved")

    df = load_data()
    X, y = prep_data(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    model = train_model(X_train, y_train)

    evaluate_model(model, X_train, X_test, y_train, y_test)
    save_model(model)

new_smart_fella()