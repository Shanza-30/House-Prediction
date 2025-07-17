from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    sqft = float(request.form['sqft'])

    # For now, let's return a dummy prediction
    # Later, you can load your RidgeModel.pkl and use it here
    predicted_price = sqft * 6000  # Dummy formula

    return f"<h2>Estimated House Price: ₹ {predicted_price:,.2f}</h2>"

if __name__ == '__main__':
    app.run(debug=True)