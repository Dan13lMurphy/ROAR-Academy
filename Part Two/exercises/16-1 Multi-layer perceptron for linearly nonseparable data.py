from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Create data
linearSeparableFlag = False
x_bias = 6


def toy_2D_samples(x_bias, linearSeparableFlag):
    label1 = np.array([[1, 0]])
    label2 = np.array([[0, 1]])

    if linearSeparableFlag:
        samples1 = np.random.multivariate_normal(
            [5 + x_bias, 0], [[1, 0], [0, 1]], 100)
        samples2 = np.random.multivariate_normal(
            [-5 + x_bias, 0], [[1, 0], [0, 1]], 100)
        samples = np.concatenate((samples1, samples2), axis=0)
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
        plt.show()
    else:
        samples1 = np.random.multivariate_normal(
            [5 + x_bias, 5], [[1, 0], [0, 1]], 50)
        samples2 = np.random.multivariate_normal(
            [-5 + x_bias, -5], [[1, 0], [0, 1]], 50)
        samples3 = np.random.multivariate_normal(
            [-5 + x_bias, 5], [[1, 0], [0, 1]], 50)
        samples4 = np.random.multivariate_normal(
            [5 + x_bias, -5], [[1, 0], [0, 1]], 50)
        samples = np.concatenate(
            (samples1, samples2, samples3, samples4), axis=0)
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
        plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
        plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
        plt.show()

    labels1 = np.repeat(np.array([[1, 0]]), 100, axis=0)
    labels2 = np.repeat(np.array([[0, 1]]), 100, axis=0)
    labels = np.concatenate((labels1, labels2), axis=0)
    return samples, labels


# Generate data
samples, labels = toy_2D_samples(x_bias, linearSeparableFlag)

# Shuffle and split
randomOrder = np.random.permutation(200)
trainingX = samples[randomOrder[:100], :]
trainingY = labels[randomOrder[:100], :]
testingX = samples[randomOrder[100:], :]
testingY = labels[randomOrder[100:], :]

# Define deeper sigmoid MLP
model = Sequential()
model.add(Dense(16, input_shape=(2,), activation='sigmoid'))
model.add(Dense(12, activation='sigmoid'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(2, activation='softmax'))

# Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(trainingX, trainingY, epochs=1000,
          batch_size=10, verbose=1, validation_split=0.2)

# Evaluate on testing set
score = 0
for i in range(100):
    predict_x = model.predict(np.array([testingX[i, :]]), verbose=0)
    estimate = np.argmax(predict_x, axis=1)
    if testingY[i, estimate] == 1:
        score += 1
    if estimate == 0:
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    else:
        plt.plot(testingX[i, 0], testingX[i, 1], 'rx')

print('Test accuracy:', score / 100)
plt.title("Test Classification Results")
plt.show()
