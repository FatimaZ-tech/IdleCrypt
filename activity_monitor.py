import time
from pynput import keyboard, mouse

last_activity = time.time()

def update_activity(*args):
    global last_activity
    last_activity = time.time()

def start_activity_monitor():
    keyboard.Listener(on_press=update_activity).start()
    mouse.Listener(on_move=update_activity).start()

def idle_seconds():
    return time.time() - last_activity
