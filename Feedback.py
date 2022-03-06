import RPi.GPIO as GPIO
from time import sleep

class Feedback():
    def __init__(self):
        self.left = 8
        self.right = 10
        self.front = 12
        self.back = 16
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.left, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.right, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.front, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.back, GPIO.OUT, initial=GPIO.LOW)
    
    def hit(self):
        GPIO.output(self.left, GPIO.HIGH)
        sleep(1)
        GPIO.output(self.left, GPIO.LOW)

    def stand(self):
        GPIO.output(self.right, GPIO.HIGH)
        sleep(1)
        GPIO.output(self.right, GPIO.LOW)

    def split(self):
        GPIO.output(self.front, GPIO.HIGH)
        sleep(1)
        GPIO.output(self.front, GPIO.LOW)

    def double(self):
        GPIO.output(self.back, GPIO.HIGH)
        sleep(1)
        GPIO.output(self.back, GPIO.LOW)

if __name__ == "__main__":
    feedback = Feedback()
    feedback.hit()
    feedback.stand()
    feedback.split()
