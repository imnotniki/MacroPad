from MacroPad import *

def printOne(msg):
    print(f"FOUND: {msg}")


if __name__ == "__main__":
    mp = MacroPad(port='/dev/ttyUSB0', baud_rate=115200)
    mp.on_message(message="1", callback=printOne)

    try:
        mp.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping listener...")
        mp.stop()