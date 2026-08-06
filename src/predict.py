from utils import (
    load_model,
    format_price,
    get_integer,
    prepare_input,
    create_history,
    save_prediction
)


def main():

    # ------------------------------
    # Load Model
    # ------------------------------

    model = load_model()

    print("\n🏠 HOUSE PRICE PREDICTION\n")

    # ------------------------------
    # User Inputs
    # ------------------------------

    area = float(input("Enter Area (sq.ft): "))

    bedrooms = get_integer("Enter Number of Bedrooms: ")

    bathrooms = get_integer("Enter Number of Bathrooms: ")

    stories = get_integer("Enter Number of Stories: ")

    mainroad = input("Main Road (Yes/No): ")

    guestroom = input("Guest Room (Yes/No): ")

    basement = input("Basement (Yes/No): ")

    hotwaterheating = input("Hot Water Heating (Yes/No): ")

    airconditioning = input("Air Conditioning (Yes/No): ")

    parking = get_integer("Enter Parking Spaces: ")

    prefarea = input("Preferred Area (Yes/No): ")

    print("\nChoose Furnishing Status")

    print("1. Furnished")
    print("2. Semi-Furnished")
    print("3. Unfurnished")

    choice = get_integer("Enter your choice (1-3): ")

    if choice == 1:
        furnishing = "Furnished"

    elif choice == 2:
        furnishing = "Semi-Furnished"

    elif choice == 3:
        furnishing = "Unfurnished"

    else:
        print("❌ Invalid Choice")
        return

    # ------------------------------
    # Prepare Input
    # ------------------------------

    new_house = prepare_input(
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
    )

    # ------------------------------
    # Prediction
    # ------------------------------

    price = model.predict(new_house)[0]

    # ------------------------------
    # Save Prediction History
    # ------------------------------

    history = create_history(
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
    )

    save_prediction(history)

    # ------------------------------
    # Display Result
    # ------------------------------

    print("\n==============================")

    print("🏠 HOUSE PRICE PREDICTION")

    print("==============================")

    print(f"\nEstimated House Price : {format_price(price)}")


if __name__ == "__main__":
    main()