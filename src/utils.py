import joblib
import pandas as pd
import os
from datetime import datetime
from pathlib import Path

# --------------------------------------------------
# Model Functions
# --------------------------------------------------

def load_model(model_path="models/house_price_model.pkl"):
    """
    Load the trained Machine Learning model.
    """
    return joblib.load(model_path)


def save_model(model):
    """
    Save the trained Machine Learning model.
    """
    joblib.dump(model, "models/house_price_model.pkl")
    print("\n✅ Model saved successfully!")


# --------------------------------------------------
# Price Formatting
# --------------------------------------------------

def format_price(price):
    """
    Format the predicted price.
    """
    return f"₹{price:,.2f}"


# --------------------------------------------------
# Integer Validation
# --------------------------------------------------

def get_integer(prompt):
    """
    Get a valid integer from the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")


# --------------------------------------------------
# Save Prediction History
# --------------------------------------------------

def save_prediction(history):
    """
    Save prediction history to a CSV file.
    """

    BASE_DIR = Path(__file__).resolve().parent.parent

    history_dir = BASE_DIR / "history"
    history_dir.mkdir(exist_ok=True)

    file_path = history_dir / "prediction.csv"

    current = datetime.now()

    history["Date"] = current.strftime("%Y-%m-%d")
    history["Time"] = current.strftime("%H:%M:%S")

    df = pd.DataFrame([history])

    if not file_path.exists() or file_path.stat().st_size == 0:
        df.to_csv(
            file_path,
            index=False
        )
    else:
        df.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )


# --------------------------------------------------
# Prepare User Input
# --------------------------------------------------

def prepare_input(
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishing
):
    """
    Convert user input into the format expected by the model.
    """

    # Convert Yes/No to 1/0
    mainroad = 1 if mainroad.lower() == "yes" else 0
    guestroom = 1 if guestroom.lower() == "yes" else 0
    basement = 1 if basement.lower() == "yes" else 0
    hotwaterheating = 1 if hotwaterheating.lower() == "yes" else 0
    airconditioning = 1 if airconditioning.lower() == "yes" else 0
    prefarea = 1 if prefarea.lower() == "yes" else 0

    # One-Hot Encoding
    furnished = 0
    semi_furnished = 0
    unfurnished = 0

    if furnishing.lower() == "furnished":
        furnished = 1

    elif furnishing.lower() == "semi-furnished":
        semi_furnished = 1

    else:
        unfurnished = 1

    new_house = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus_furnished": [furnished],
        "furnishingstatus_semi-furnished": [semi_furnished],
        "furnishingstatus_unfurnished": [unfurnished]
    })

    return new_house


# --------------------------------------------------
# Create Prediction History
# --------------------------------------------------

def create_history(
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishing,
    price
):
    """
    Create a prediction history dictionary.
    """

    history = {
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Stories": stories,
        "Parking": parking,
        "Main Road": mainroad,
        "Guest Room": guestroom,
        "Basement": basement,
        "Hot Water Heating": hotwaterheating,
        "Air Conditioning": airconditioning,
        "Preferred Area": prefarea,
        "Furnishing": furnishing,
        "Predicted Price": price
    }

    return history

