import matplotlib.pyplot as plt
import numpy as np

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)


def stepFunction(t):
    return t >= 0


def prediction(X, W, b):
    return stepFunction((np.matmul(X, W) + b)[0])


# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate=0.01):
    # Fill in code
    # p_pred = np.matmul(X, W) + b
    # p_pred[p_pred >= 0] = 1
    # p_pred[p_pred < 0] = 0

    for i in range(X.shape[0]):
        x = X[i]
        pred = prediction(x, W, b)
        x = x.reshape(-1, 1)

        if pred != y[i]:
            if pred == 0:
                W += x * learn_rate
                b += learn_rate
            else:
                W -= x * learn_rate
                b -= learn_rate

    return W, b


# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate=0.01, num_epochs=25):
    print(X, y)

    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2, 1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0] / W[1], -b / W[1]))
    return boundary_lines


if __name__ == '__main__':
    data = np.genfromtxt('data.csv', delimiter=',')
    X = data[:, :-1]
    Y = data[:, -1]

    color = list(map(lambda x: 'red' if x == 0 else 'blue', Y))

    plt.scatter(X[:, 0], X[:, 1], c=color)

    boundaries = trainPerceptronAlgorithm(X, Y)

    plt.

    plt.show()
