import time
import board
import busio
import digitalio

from MyButton import *


keys = ["1", "2", "3"]
uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=1)


def printHi():
    counter = 2
    print("Hi triggered")
    message = keys[counter % 3]
    uart.write(message.encode('utf-8'))

def printNone():
    pass
bt1 = MyButton(board.IO4, printHi)
bt2 = MyButton(board.IO5, printNone)


buttons = [bt1, bt2]
def send_data():
    counter = 0
    while True:
        for button in buttons:
            button.update()
        time.sleep(0.1)


if __name__ == "__main__":
    send_data()


