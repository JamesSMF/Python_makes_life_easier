import Neu_import.py

# Callbacks
early_stopping = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', 
                                                   patience=3, 
                                                   restore_best_weights=True)]

# Using SimpleRNN
def build_rnn(size, embedding_dim, max_length):
    model_rnn = Sequential()
    model_rnn.add(Embedding(size, 
                            embedding_dim, 
                            input_length=max_length))
    model_rnn.add(Dropout(0.5))
    model_rnn.add(SimpleRNN(64, kernel_regularizer=l2(0.0001)))
    model_rnn.add(Dropout(0.5))
    model_rnn.add(Dense(1, activation='sigmoid'))
    model_rnn.compile(loss='binary_crossentropy', 
                  optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), 
                  metrics = ['accuracy'])
    return model_rnn
