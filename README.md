# Pylogger2
## Simple keylogger
![before_filter](https://user-images.githubusercontent.com/90658763/190903395-2cd84e6e-a270-4dd8-ab4b-78a2d0b23797.gif)

# Functions:
## This code uses Python's pynput library to capture the keys that are pressed on the keyboard and write them to an activity log file (log.txt). In short, the code acts as a keylogger.

### When a key is pressed, the on_press function is called, and the key is added to the keys list. If 10 or more keys have been pressed, the keys list is written to the log.txt file by the ```write_file``` function, and the keys list and counter are reset. The ```write_file``` function takes the list of keys and writes each key to a separate line in the log file, formatted appropriately so that it is easy to read.

### The ```on_release"```  function is called when a key is released, and in this case it does nothing special other than exit the program if the "esc" key is pressed.

# Bookstores:

## Pynut:
[![PYAUTOGUI](https://user-images.githubusercontent.com/90658763/230070764-d9e57eed-83eb-4c05-a1a4-be008381420e.png)](https://pypi.org/project/pynput/)

## Sequential:

[![PYAUTOGUI](https://user-images.githubusercontent.com/90658763/235352072-c25a3a31-02f0-4622-b629-f796235e4a51.png)](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential)

## Dense:
[![PYAUTOGUI](https://user-images.githubusercontent.com/90658763/235354635-4ecd2bc3-3d14-4110-a17a-290dcf3558ea.png)](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)

## Adam:
[![PYAUTOGUI](https://user-images.githubusercontent.com/90658763/235354727-77de3018-871b-4688-84e0-003ab97c9567.png)](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam)

## Sparse_categorical_crossentropy:
[![PYAUTOGUI](https://user-images.githubusercontent.com/90658763/235354808-227f0453-d17c-4c9a-ab96-7d1c4135563e.png)](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/sparse_categorical_crossentropy)
![image](https://user-images.githubusercontent.com/90658763/236671860-95761804-9113-4642-843d-15f9d7d374de.png)

