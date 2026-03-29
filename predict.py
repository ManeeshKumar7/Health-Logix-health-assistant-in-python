import pickle
import numpy as np

model = pickle.load(open('../models/health_model.pkl','rb'))

def predict(bmi,activity,sleep,heart_rate):
    data = np.array([[bmi,activity,sleep,heart_rate]])
    risk = model.predict(data)[0]

    if risk==0:
        return "Healthy lifestyle"
    elif risk==1:
        return "Moderate risk - improve habits"
    else:
        return "High risk - consult doctor"
