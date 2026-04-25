import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data=pd.read_csv('Flask and model intergration/Crop_recommendation.csv')
x=data.iloc[:,:-1] #features
y=data.iloc[:,-1] #label
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=RandomForestClassifier()
model.fit(x_train,y_train)
pickle.dump(model,open('model.pkl','wb'))
