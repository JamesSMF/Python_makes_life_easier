# TensorFlow
%tensorflow_version 2.x
import tensorflow as tf

# Proprocessing tools
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Keras models and layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM, GRU
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Reshape

# Scientific computing
import numpy as np

# Regularizers
from tensorflow.keras.regularizers import l2

# Plotting
import matplotlib.pyplot as plt

def plot_graphs(history, string):
    '''
    Plot training acc/loss and validation acc/loss
    '''
    plt.plot(history.history[string])
    plt.plot(history.history['val_'+string])
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, 'val_'+string])
    plt.show()
