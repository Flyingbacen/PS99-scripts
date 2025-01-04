import keyboard
import pydirectinput
import threading
from pyautogui import pixelMatchesColor

pydirectinput.PAUSE = 0.05
running = True

def main():
    global running
    while running:
        pydirectinput.press("e")
        pydirectinput.leftClick(815, 697)

def stop():
    global running
    print("Exiting...")
    running = False

main_thread = threading.Thread(target=main)

print("f3 to start\nf8 to stop\n")
keyboard.add_hotkey("f3", lambda: main_thread.start())
keyboard.add_hotkey("f8", lambda: [stop(), main_thread.join()])
keyboard.wait("f8")