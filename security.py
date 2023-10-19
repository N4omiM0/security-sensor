import time
import board
import neopixel
import digitalio as dio
import adafruit_hcsr04
from adafruit_led_animation.color import (RED, YELLOW, GREEN, BLACK)

pixel_pin = board.D2
pixel_num = 30
np = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

buttonArm = dio.DigitalInOut(board.D3)
buttonArm.direction = dio.Direction.INPUT
buttonDisarm = dio.DigitalInOut(board.D4)
buttonDisarm.direction = dio.Direction.INPUT

bb = dio.DigitalInOut(board.D5)
bb.direction = dio.Direction.INPUT
bb.pull = dio.Pull.UP

pir = dio.DigitalInOut(board.D6)
pir.direction = dio.Direction.INPUT

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)

armed = False
'''This function sets the arming phase. The neopixels turn yellow for 10 seconds, then after,
    the neopixels turn red and it is armed.'''
def arm():
    global armed
    print("Arming")
    np.fill(YELLOW)
    np.show()
    time.sleep(10)
    np.fill(RED)
    np.show()
    armed = True
    print("Armed")
'''This function disarms the system. The noepixels turn green, and when the sensors are triggered,
    nothing happens.'''
def disarm():
    global armed
    np.fill(GREEN)
    np.show()
    armed = False
    print("Disarmed")
'''This is the trigger function. When the sensors are triggered, the neopixels blink red.'''
def trigger():
    for i in range(10):
        np.fill(BLACK)
        np.show()
        time.sleep(0.5)
        np.fill(RED)
        np.show()
        time.sleep(0.5)

while True:
    try:
        distance = sonar.distance
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    if buttonArm.value == False:
        arm()
    if buttonDisarm.value == False:
        disarm()
    if armed == True:
        if pir.value:
            time.sleep(3)
            print("PIR Trigger")
            trigger()
            time.sleep(1)
        if distance >= 75:
            print("Sonar Trigger")
            trigger()
            time.sleep(1)
        if not bb.value:
            print("Break Beam Trigger")
            trigger()
            time.sleep(1)

