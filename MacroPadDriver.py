import serial
import time
import serial.tools.list_ports
import pyautogui

class MacropadDriver:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        self.port = None
        if port:
            self.port = port
        else:
            self.port = self.findPort()
        self.baudrate = baudrate
        self.timeout = timeout

    def findPort(self):
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "JTAG" in port.description:
                return port.device
        return None

    def listen(self):
        try:
            with serial.Serial(self.port, self.baudrate, timeout=self.timeout) as ser:
                print(f"Listening on {self.port}...")
                while True:
                    if ser.in_waiting > 0:
                        message = ser.readline().decode('utf-8').strip()
                        if message == "2":
                            pyautogui.moveTo(20, 20)
                        print(f"Received: {message}")
                    time.sleep(0.1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    mpd = MacropadDriver()
    mpd.listen()
