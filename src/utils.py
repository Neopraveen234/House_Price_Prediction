import joblib
import pandas as pd
import os
from datetime import datetime

def load_model(model_path="models/house_price_model.pkl"):
    """
    Load the trained model.
    """
    return joblib.load(model_path)

def save_model(model):
    """
    Save the trained models.
    """

    joblib.dump(model,"models/house_price_model.pkl")

    print("\n✅Model saved successfully!!!")


def format_price(price):
    """
    Return a formatted price string.
    """
    return f"₹{price:,.2f}"


def get_integer(prompt):
    """
    Get a Valid integer from the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌Invalid input! Please enter a whole number.")



def save_prediction(history):
    """
    Save prediction history into a CSV file.
    """

    file_path="history/prediction.csv"

    current=datetime.now()

    history['Date']=current.strftime("%Y-%m-%d")
    history['Time']=current.strftime("%H:%M:%S")

    df=pd.DataFrame([history])

    if os.path.exists(file_path):
        df.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            file_path,
            index=False
        )