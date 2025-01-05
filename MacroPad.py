import serial
import threading
import time

class MacroPad:

    DEBUG_MODE = True

    def __init__(self, port, baud_rate=115200):
        self.port = port
        self.baud_rate = baud_rate
        self.callbacks = []
        self.running = False
        self.thread = None

    def start(self):
        if self.running:
            print("Listener is already running.")
            return

        self.running = True
        self.thread = threading.Thread(target=self._listen, daemon=True)
        self.thread.start()
        print(f"Listening on {self.port} at {self.baud_rate} baud...")

    def stop(self):
        if not self.running:
            print("Listener is not running.")
            return

        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
        print("Listener stopped.")

    def on_message(self, message, callback):
        self.callbacks.append((message, callback))
        print(f"Callback registered for message: {message}")

    def _listen(self):
        try:
            with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:
                ser.reset_input_buffer()
                time.sleep(2)
                while self.running:
                    if ser.in_waiting > 0:
                        line = ser.readline().decode('utf-8').strip()
                        for message, callback_function in self.callbacks:
                            if line == message:
                                callback_function(line)
                        if self.DEBUG_MODE:
                            print(f"DEBUG RECEIVED MESSAGE: {line}")
                    time.sleep(0.1)
        except serial.SerialException as e:
            print(f"Serial error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.running = False



