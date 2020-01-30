'''
linear_reg.py
This is a program modeling linear regression.
Basic steps:
   1. Generate x data set, and add some noise to make data scattered.
   2. Modeling: use Sequential() to build a linear model with both input and
      output dimension being 1.
   3. Training models: Train the model on batches to update gradient. You will
      see the loss (i.e. the cost) of training gets smaller, which means the
      prediction becomes more accurate with larger number of data.
   4. Get the weight and bias from the training results.
   5. Generate a prediction linear function according to the weight and bias:
      y_predict = weight * x + bias
   6. Plot the line.

Note:
   This program is not intended to be run on terminal (Jupyter would be a nice choice).
'''


import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

# Generate Dataset
x_data = np.random.rand(100)
noise = np.random.normal(0, 0.01, x_data.shape)
y_data = x_data*0.1 + 0.2 + noise

# plot
plt.scatter(x_data, y_data)
plt.show

# Modeling
model = Sequential()
model.add(Dense(units=1, input_dim=1))
# sgd: Stochastic Gradient Descent
# mse: Mean Squared Error
model.compile(optimizer="sgd", loss="mse")

# Training
for step in range(3001):
   cost = model.train_on_batch(x_data, y_data)
   if step % 500 == 0:
      print("cost", cost)

# Get weight and bias
W, b = model.layers[0].get_weights()
print("Weight: ", W, " Bias: ", b)

# Predict y value using x data set
y_pred = model.predict(x_data)
y_std = x_data*0.1 + 0.2

# plot
plt.scatter(x_data, y_data)
plt.plot(x_data, y_pred, 'r-', lw=1)     # Predicted data model
plt.plot(x_data, y_std, 'g-', lw=1)      # Actual data model
plt.show
