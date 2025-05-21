# Titanic survival prediction function
def predict_survival(passenger):
    """
    Predict survival based on passenger features.
    :param passenger: A dictionary containing passenger's details
    :return: 'Survived' or 'Did not survive'
    """
    # Example conditions for survival prediction
    if passenger["Sex"] == "female":
        return "Survived"
    elif passenger["Pclass"] == 1 and passenger["Age"] < 18:
        return "Survived"
    else:
        return "Did not survive"

# Example passenger data
passenger1 = {
    "Pclass": 1,  # Passenger class (1 = First, 2 = Second, 3 = Third)
    "Sex": "male",  # Gender (male or female)
    "Age": 25      # Age in years
}

passenger2 = {
    "Pclass": 3,
    "Sex": "female",
    "Age": 30
}

# Predict survival
print(f"Passenger 1: {predict_survival(passenger1)}")
print(f"Passenger 2: {predict_survival(passenger2)}")

