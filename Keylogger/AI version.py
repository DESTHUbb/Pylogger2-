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
    
# Create a dictionary to assign each severity level to an integer index
label_to_index = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}

# Convert the text labels to integers using the dictionary above
y = [label_to_index[label] for label in y]

# Create a dictionary of words to assign each unique word to an integer index
vocab = {}
index = 1
for log in  X:
    words = log.split()
    for word in words:
        if word not in vocab:
            vocab[word] = index
            index += 1      
      
# Convert each input record to a sequence of integers using the word dictionary
X_int = []
for log in X:
    words = log.split()
    X_int.append([vocab[word] for word in words])
 
# We configure some parameters of the model
voca_size = len(vocab) + 1
output_size = len(label_to_index)
embedding_size = 128
hidden_size = 256

# Create the neural network model
model = Sequential()
model.add(Dense(embedding_size, input_shape=(None,)))



