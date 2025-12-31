import pickle

with open("study_time_predictor.pkl", "rb") as f:
    model = pickle.load(f)

def predict_hours(marks, difficulty, days_left):
    result = model.predict([[marks, difficulty, days_left]])
    return round(result[0], 2)
