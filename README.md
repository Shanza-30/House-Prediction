# 🏠 Bangalore House Price Prediction Web Application

This project is a **full-stack machine learning web application** built using **Flask**, designed to predict **house prices in Bangalore** based on user-provided inputs. It demonstrates seamless integration of a trained ML model with a responsive web interface.


## 🎯 Project Objective

The application helps users, home buyers, and real estate enthusiasts estimate property prices in Bangalore using historical housing data, enabling informed decisions based on real-world trends.


## 🧠 Machine Learning Model

* **Model Used:** Ridge Regression
* **Training Data:** `Cleaned_data.csv` containing:

  * Location
  * Square Footage
  * Number of Bathrooms
  * Number of BHKs
* **Preprocessing Steps:**

  * Handling missing values
  * Encoding categorical features (like location)
  * Normalizing numerical values
* **Model Deployment:** The trained model is saved as `RidgeModel.pkl` and loaded during runtime for instant predictions.


## 🌐 User Interface

* Built using **HTML, CSS, and Bootstrap** for a clean and responsive design
* **Input Fields:**

  * Location (dropdown menu)
  * Number of Bedrooms (BHK)
  * Number of Bathrooms
  * Total Area (in sq. ft.)
* **Prediction:** On submission, the app processes user inputs and displays the estimated house price instantly.


## 🛠 Technologies Used

* Python
* Flask
* Pandas & NumPy
* scikit-learn (Ridge Regression)
* HTML, CSS, Bootstrap
* Pickle (for saving/loading the model)


## ✨ Key Features

* User-friendly web interface for real-time house price estimation
* Preprocessing and encoding of user inputs for accurate predictions
* Instant output of estimated prices
* Practical demonstration of **ML deployment in a web app**


## 🔮 Future Enhancements

* Include additional features like property age, floor number, and amenities
* Deploy on cloud platforms like Heroku or Render for public access
* Add visualizations for price trends across locations
* Integrate alternative regression models for comparative analysis


## 📌 Conclusion

This project showcases the **practical integration of machine learning with web development**, providing a real-world example of a **predictive web application**. It demonstrates how historical data and regression modeling can deliver instant, actionable insights for users in the real estate domain.
