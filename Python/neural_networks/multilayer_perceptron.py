import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))


# Network size
N_input = 4
N_hidden = 3
N_output = 2

np.random.seed(42)
# Make some fake data
X = np.random.randn(4)

weights_input_to_hidden = np.random.normal(0, scale=0.1, size=(N_input, N_hidden))
weights_hidden_to_output = np.random.normal(0, scale=0.1, size=(N_hidden, N_output))

hidden_layer_in = X
hidden_layer_out = sigmoid(np.dot(hidden_layer_in, weights_input_to_hidden))

print('Hidden-layer Output:')
print(hidden_layer_out)

output_layer_in = hidden_layer_out
output_layer_out = sigmoid(np.dot(output_layer_in, weights_hidden_to_output))

print('Output-layer Output:')
print(output_layer_out)
