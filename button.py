import board
import neopixel
import digitalio as dio
import time
np = neopixel.NeoPixel(board.D2, 30, brightness=0.5, auto_write=True)

buttonArm = dio.DigitalInOut(board.D4)
buttonArm.direction = dio.Direction.INPUT
buttonDisarm = dio.DigitalInOut(board.D5)
buttonDisarm.direction = dio.Direction.INPUT

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

armed = False


def arm():
    global armed
    np.fill(YELLOW)
    np.show()
    time.sleep(10)
    for i in range(10):
        if i % 2 == 0:
            np.fill(RED)
        else:
            np.fill(BLACK)
        np.show()
        time.sleep(1)
        
    armed = True
    print(armed)

def disarm():
    global armed
    np.fill(GREEN)
    np.show()
    armed = False
    print(armed)
    time.sleep(.5)

while True:
    np.fill(GREEN)
    if buttonArm.value == False:
        arm()
    if buttonDisarm.value == False:
        disarm()
