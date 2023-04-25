# Example of using a neural network to classify log messages for PyLogging

from tensorflow, keras, models import Sequential
from tensorflow, keras, layers import Dense
from tensorflow, keras, optimizers import Adam
from tensorflow, keras, losses import sparse_categorical_crossentropy

# Load the training records
with open("training_logs.txt", "r") as f:
    training_logs = f.readlines()

# We divide the records into examples of input (X) and output (y)
X = []
Y = []
for log in training_logs:
     parts = log.split("|")
    X.append(parts[0])
    y.append(int(parts[1]))

    
