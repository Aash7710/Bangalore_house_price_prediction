import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, total_sqft, bath, balcony, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict using the model and convert to float
    predicted_price = __model.predict([x])[0]
    return float(round(predicted_price, 2))


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    # Update the path as per your project structure
    with open("C:\\Users\\aashp\\OneDrive\\Desktop\\flask\\House price prediction\\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    global __model
    if __model is None:
        # Update the path as per your project structure
        with open(
                "C:\\Users\\aashp\\OneDrive\\Desktop\\flask\\House price prediction\\banglore_home_prices_model.pickle",
                'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Block Jayanagar', 1875, 2, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 1, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 3, 2))
