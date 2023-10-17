
import board
import neopixel
import digitalio as dio
import adafruit_hcsr04
import time
import random
from adafruit_led_animation.animation.blink import Blink

alert_btn = dio.DigitalInOut(board.D5)
disarm_btn = dio.DigitalInOut(board.D6)
alert_btn.direction = dio.Direction.INPUT
disarm_btn.direction = dio.Direction.INPUT
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D4)
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness=0.25)

red = [255,0,0]
yellow = [255,255,0]
green = [0,255,0]
off = [0,0,0]
distance = sonar.distance

armed = False

def arm():
    global armed
    np.fill(off)
    np.show()
    time.sleep(0.5)
    np.fill(yellow)
    np.show()
    time.sleep(10)
    np.fill(red)
    np.show()
    armed = True
    print(armed)

def disarm():
    global armed
    np.fill(green)
    np.show()
    armed = False
    print(armed)

while True:
    if alert_btn.value == False:
        try:
            if sonar.distance >= 100:
                np.fill(green)
                np.show()
            elif sonar.distance > 25 and sonar.distance < 99
                np.fill(red)
                np.show()
        except RuntimeError:
            print("Retrying!")
    time.sleep(0.1)
    if disarm_btn.value == False:
        disarm()
        
        
    """
    try:
        if sonar.distance >= 100:
            np.fill(disarmed)
            np.show()
        else if sonar.distance > 25 and sonar.distance <    
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    """
