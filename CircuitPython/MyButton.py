import digitalio

class MyButton:

    def __init__(self, PIN, callback):
        self.button = digitalio.DigitalInOut(PIN)
        self.button.switch_to_input(pull=digitalio.Pull.UP)
        self.pressed = False
        self.callback = callback


    def update(self):
        if not self.button.value:
            if not self.pressed:
                self.pressed = True
            if self.pressed:
                self.callback()
        if self.button.value:
            if self.pressed:
                self.pressed = False
