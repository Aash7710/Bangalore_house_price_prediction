from flask import Flask, request, jsonify
import utility
import traceback

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = utility.get_location_names()
        response = jsonify({
            'locations': locations
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Extract data from the POST request
        total_sqft = float(request.form.get('total_sqft', 0))
        location = request.form.get('location', '')
        bhk = int(request.form.get('bhk', 0))
        bath = int(request.form.get('bath', 0))
        balcony = int(request.form.get('balcony', 0))

        # Debugging: Print received values
        print(f"Received - Sqft: {total_sqft}, Location: {location}, BHK: {bhk}, Bath: {bath}, Balcony: {balcony}")

        # Get the estimated price from the utility module
        estimated_price = utility.get_estimated_price(location, total_sqft, bath, balcony, bhk)

        # Debugging: Print the estimated price and its type
        print(f"Estimated Price: {estimated_price} (Type: {type(estimated_price)})")

        # Prepare the JSON response
        response = jsonify({
            'estimated_price': estimated_price  # This is already a standard float
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        # Print the traceback for debugging purposes
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    utility.load_saved_artifacts()
    app.run(debug=True)
