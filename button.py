import board
import neopixel
import digitalio as dio
import time
np = neopixel.NeoPixel(board.D2, 30, brightness=0.5, auto_write=True)

#buttons
alert_btn = dio.DigitalInOut(board.D4)
disarm_btn = dio.DigitalInOut(board.D5)

alert_btn.direction = dio.Direction.INPUT
disarm_btn.direction = dio.Direction.INPUT

#alert colors
armed = (255, 0, 0)
arming = (255, 255, 0)
off = (0, 255, 0)

while True:
  np.fill(off)
  if alert_btn.value:
    np.fill(arming)
    time.sleep(10)
    np.fill(armed)
    if disarm_btn.value:
      np.fill(off)
        
    
