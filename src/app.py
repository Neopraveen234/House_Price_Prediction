import os
import pandas as pd
import streamlit as st

from utils import (
    load_model,
    format_price,
    prepare_input,
    create_history,
    save_prediction
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = load_model()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🏠 House Price Prediction")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Predict House Price",
        "📜 Prediction History",
        "ℹ️ About"
    ]
)

# ==================================================
# PAGE 1 : PREDICT HOUSE PRICE
# ==================================================

if page == "🏠 Predict House Price":

    st.title("🏠 House Price Prediction")

    st.write(
        "Enter the details below to predict the estimated price of a house."
    )

    st.divider()

    # ------------------------------
    # User Inputs
    # ------------------------------
    col1,col2=st.columns(2)

    with col1:
        area = st.text_input(
        "Area (sq.ft)",
        placeholder="Example: 7420"
    )

    with col2:
        bedrooms = st.text_input(
        "Number of Bedrooms",
        placeholder="Example: 3"
    )
    with col1:
        bathrooms = st.text_input(
        "Number of Bathrooms",
        placeholder="Example: 2"
    )
    with col2:
        stories = st.text_input(
        "Number of Stories",
        placeholder="Example: 2"
    )
    with col1:
        mainroad = st.selectbox(
        "Main Road Access",
        ["Yes", "No"]
    )
    with col2:
        guestroom = st.selectbox(
        "Guest Room",
        ["Yes", "No"]
    )
    with col1:
        basement = st.selectbox(
        "Basement",
        ["Yes", "No"]
    )
    with col2:
        hotwaterheating = st.selectbox(
        "Hot Water Heating",
        ["Yes", "No"]
    )
    with col1:
        airconditioning = st.selectbox(
        "Air Conditioning",
        ["Yes", "No"]
    )
    with col2:
        parking = st.text_input(
        "Parking Spaces",
        placeholder="Example: 2"
    )
    with col1:
        prefarea = st.selectbox(
        "Preferred Area",
        ["Yes", "No"]
    )
    with col2:
        furnishing = st.selectbox(
        "Furnishing Status",
        [
            "Furnished",
            "Semi-Furnished",
            "Unfurnished"
        ]
    )

    st.divider()

    predict = st.button("🔍 Predict Price")

    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    if predict:

        # Validate Inputs
        try:
            area = float(area)
            bedrooms = int(bedrooms)
            bathrooms = int(bathrooms)
            stories = int(stories)
            parking = int(parking)

        except ValueError:
            st.error("❌ Please enter valid numeric values.")
            st.stop()

        # Prepare Input
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

        # Predict Price
        price = model.predict(new_house)[0]

        # Display Result
        st.success("✅ Prediction Completed Successfully!")

        st.divider()

        st.subheader("🏠 Prediction Result")

        col1,col2=st.columns(2)
        with col1:
         st.metric(
            label="Estimated Price",
            value=format_price(price)
        )

        with col2:
            st.metric(
                label="Model",
                value="Linear Regression"
            )

        st.divider()


        # Create History
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

        # Save History
        save_prediction(history)

# ==================================================
# PAGE 2 : PREDICTION HISTORY
# ==================================================

elif page == "📜 Prediction History":

    st.title("📜 Prediction History")

    st.write("View all previously predicted house prices.")

    st.divider()

    history_file = "history/prediction.csv"

    if os.path.exists(history_file):

        history_df = pd.read_csv(history_file)

        total_predictions=len(history_df)
        average_price=history_df['Predicted Price'].mean()
        highest_price=history_df['Predicted Price'].max()
        lowest_price=history_df['Predicted Price'].min()

        col1, col2,col3,col4=st.columns(4)

        with col1:
            st.metric(
                "Total Predictions",
                total_predictions
            )

        with col2:
            st.metric(
                "Average Price",
                format_price(average_price)
            )

        with col3:
            st.metric(
                "Highest Price",
                format_price(highest_price)
            )

        with col4:
            st.metric(
                "Lowest Price",
                format_price(lowest_price)
            )

        st.dataframe(
            history_df,
            use_container_width=True
        )

        if st.button("🗑️ Clear Prediction History"):

            if os.path.exists(history_file):
                os.remove(history_file)

                st.success("Prediction history cleared successfully.")

                st.rerun()

    else:
        st.info("No prediction history available.")


# ==================================================
# PAGE 3 : ABOUT
# ==================================================

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.divider()

    st.header("🏠 House Price Prediction")

    st.write(
        """
        This Machine Learning application predicts the price of a house
        based on various property features entered by the user.
        The prediction is generated using a trained Linear Regression model.
        """
    )

    st.divider()

    st.subheader("🤖 Machine Learning Model")

    st.markdown("""
- **Algorithm:** Linear Regression
- **Library:** Scikit-learn
- **Programming Language:** Python
""")

    st.subheader("📊 Dataset")

    st.markdown("""
- Housing Dataset
- **545 House Records**
- **12 Input Features**
- Target Variable: **Price**
""")

    st.subheader("🛠 Technologies Used")

    st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
""")

    st.subheader("✨ Features")

    st.markdown("""
- House Price Prediction
- Prediction History
- Dashboard Statistics
- Download Prediction History
- Responsive Streamlit Interface
""")

    st.subheader("👨‍💻 Developer")

    st.markdown("""
**Praveenkanth M**

Machine Learning Enthusiast | Python Developer
""")

    st.subheader("🔗 Connect With Me")

    st.markdown("""
**GitHub:**  
https://github.com/Neopraveen234

**LinkedIn:**  
https://www.linkedin.com/in/praveenkanth-m
""")

    st.divider()

    st.success("Version 1.0")				