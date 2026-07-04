from sklearn.linear_model import LinearRegression
import numpy as np

x = [1,2,3,4,5]
y = [7,14,15,18,19]

x = np.array(x).reshape(-1,1)

model = LinearRegression()

model.fit(x,y)

prediction = model.predict([[10]])
print("Prediction:", prediction)
