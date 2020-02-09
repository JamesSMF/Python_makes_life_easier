'''
non_linear_reg.py

Key notes:
   1. Default optimizer sgd uses learning rate of 0.01, which is too small.
      So we can self-define the learning rate at 0.3.
   2. We add a hidden layer consisting of 10 neurons.
   3. The default activation function is linear function. We need to specify
      our own function to make it work for curves.
'''

import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# Generate 200 points evenly distributed on [-0.5, 0.5]
x_data = np.linspace(-0.5, 0.5, 200)
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise

# plot
plt.scatter(x_data, y_data)
plt.show()

# Modeling
model = Sequential()
# Build an 1-10-1 neural network
# input -> hidden
model.add(Dense(units=10, input_dim=1, activation="tanh"))
# hidden -> output
model.add(Dense(units=1, activation="tanh"))
# sgd: Stochastic Gradient Descent
# mse: Mean Squared Error
# lr: learning rate (defualt is 0.01, which would be too small for
#     non-linear models)
sgd = SGD(lr=0.3)
model.compile(optimizer=sgd, loss="mse")

# Training
for step in range(6001):
   cost = model.train_on_batch(x_data, y_data)
   if step % 1000 == 0:
      print("loss: ", cost)

# Predict y value using x value
y_pred = model.predict(x_data)
y_std = np.square(x_data)

# plot
plt.scatter(x_data, y_data)
plt.plot(x_data, y_pred, 'r-', lw=1.5)     # Predicted data model
plt.plot(x_data, y_std, 'g-', lw=1)        # Actual curve
plt.show


