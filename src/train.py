import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from utils import save_model
from config import DATA_PATH,TEST_SIZE,RANDOM_STATE


def load_data():
    """
    Load the housing dataset.
    """
    return pd.read_csv(DATA_PATH)

def preprocess_data(df):
    """
    Preprocess the dataset by encoding categorical features.
    """

    binary_columns=[
        "mainroad",
        "guestroom",
        "basement",
        "hotwaterheating",
        "airconditioning",
        "prefarea"
    ]

    for col in binary_columns:
        df[col]=df[col].map({"yes":1,"no":0})

    df=pd.get_dummies(
        df,
        columns=["furnishingstatus"],
        dtype=int
    )
    return df

def split_data(df):
    """
    Split the dataset into training and testing sets.
    """

    X=df.drop("price",axis=1)
    y=df['price']

    X_train,X_test,y_train,y_test=train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    return X_train,X_test,y_train,y_test


def train_model(X_train,y_train):
    """
    Train the Linear Regression Model.
    """

    model=LinearRegression()
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_test,y_test):
    """
    Evaluate the trained model.
    """

    y_pred=model.predict(X_test)

    mae=mean_absolute_error(y_test,y_pred)
    mse=mean_squared_error(y_test,y_pred)
    rmse=mse**0.5
    r2=r2_score(y_test,y_pred)

    print("\n===== Model Evaluation =====")
    print(f"MAE:{mae:.2f}")
    print(f"MSE:{mse:.2f}")
    print(f"RMSE:{rmse:.2f}")
    print(f"R2:{r2:.4f}")
    return y_pred


def main():
    df=load_data()
    pd.set_option("display.max_columns",None)
    df=preprocess_data(df)

    X_train,X_test,y_train,y_test=split_data(df)


    model=train_model(X_train,y_train)

    evaluate_model(model,X_test,y_test)

    save_model(model)


if __name__=="__main__":
   main()