This project is a complete end-to-end machine learning web application built using Flask, designed to predict house prices in Bangalore based on user input. It uses a trained Ridge Regression model and a cleaned dataset (Cleaned_data.csv) containing location, square footage, number of bathrooms, and number of BHKs.

The user interface is built with HTML, CSS, and Bootstrap, providing a responsive and user-friendly experience. Users can select a location from a dropdown, input the number of bedrooms and bathrooms, and specify the total area in square feet. Upon submission, the app processes the inputs and instantly displays the estimated house price.

The model itself was trained on real Bangalore housing data and includes preprocessing steps such as handling missing values, encoding categorical features (like location), and normalizing numerical values. The .pkl file (RidgeModel.pkl) is used for serving predictions.

This project showcases practical integration of machine learning with web development, making it a great demonstration of full-stack ML deployment.
