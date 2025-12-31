import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

print("🔥 Training started")

data = pd.read_csv("student_data.csv")
print("✅ CSV loaded")

X = data[['marks', 'difficulty', 'days_left']]
y = data['study_hours']

model = LinearRegression()
model.fit(X, y)

with open("study_time_predictor.pkl", "wb") as f:
    pickle.dump(model, f)

print("🎉 Model trained and .pkl file created")
