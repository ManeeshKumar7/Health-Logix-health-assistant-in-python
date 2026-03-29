import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.DataFrame({
    'bmi':[18,22,27,31,35],
    'activity':[3,4,2,1,0],
    'sleep':[7,8,6,5,4],
    'heart_rate':[70,68,75,85,95],
    'risk':[0,0,1,1,2]
})

X = data.drop('risk', axis=1)
y = data['risk']

model = RandomForestClassifier()
model.fit(X,y)

with open('../models/health_model.pkl','wb') as f:
    pickle.dump(model,f)

print("Model trained!")
