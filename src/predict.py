import pandas as pd
import joblib

from utils import (load_model,format_price,get_integer,save_prediction)
def main():
    model=load_model()
    print("🏠House Price Prediction")

    area=float(input("Enter the area (sq.ft):"))
    bedrooms=get_integer("Enter Number of Bedrooms:")
    bathrooms=get_integer("Enter Number of Bathrooms:")
    stories=get_integer("Enter Number of Stories:")
    mainroad=input("Is the house on the Main Road? (yes/No):").lower()
    guestroom=input("Does the house have a Guest Rooms? (yes/No):").lower()
    basement=input("Does the house have a Basements? (yes/No):").lower()
    hotwaterheating=input("Hot water heating available? (yes/No):").lower()
    airconditioning=input("Air conditioning available? (yes/No):").lower()
    parking=get_integer("Enter Number of Parking Spaces:")
    prefarea=input("Is it in a Preferred Area? (yes/No):").lower()

    print("\nChoose Furnishing Status")
    print("1. Fully Furnished")
    print("2.Semi-Furnished")
    print("3.Unfurnished")


    choice=get_integer("Enter your choice(1-3):")

    mainroad=1 if mainroad=="yes" else 0
    guestroom=1 if guestroom=='yes' else 0
    basement=1 if basement=='yes' else 0
    hotwaterheating=1 if hotwaterheating=='yes' else 0
    airconditioning=1 if airconditioning=='yes' else 0
    prefarea=1 if prefarea=='yes' else 0


    furnished=0
    semi_furnished=0
    unfurnished=0
    if choice==1:
        furnished=1
    elif choice==2:
        semi_furnished=1
    elif choice==3:
        unfurnished=1

    else:
        print("Invalid Choice")



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

    price=model.predict(new_house)[0]

    history={
        "Area":area,
        "Bedrooms":bedrooms,
        "Bathrooms":bathrooms,
        "Stories":stories,
        "Parking":parking,
        "Main Road":"Yes" if mainroad else "No",
        "Guest Room":"Yes" if guestroom else "No",
        "Basement":"Yes" if basement else "No",
        "Hot Water Heating":"Yes" if hotwaterheating else "No",
        "Air Conditioning":"Yes" if airconditioning else "No",
        "prefarea":"Yes" if prefarea else "No",
        "Furnishing":(
            "Furnished" if furnished else "Semi-Furnished" if semi_furnished else "Unfurnished"
        ),
        "Predicted Price":price
    }
    save_prediction(history)

    print('🏠 House Price Prediction')
    print(f"Predicted House Price:{format_price(price)}")

if __name__=="__main__":
   main()