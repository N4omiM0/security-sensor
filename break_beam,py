import board
import neopixel
import digitalio as dio
import time
np = neopixel.NeoPixel(board.D2, 30, brightness=0.5, auto_write=True)


#alert colors
armed = (255, 0, 0)
arming = (255, 255, 0)
off = (0, 255, 0)

#break beam
break_beam = dio.DigitalInOut(board.D3)
break_beam.direction = dio.Direction.INPUT
break_beam.pull = dio.Pull.UP


while True:
    np.fill(off)
    if not break_beam.value:
        print('alarm is tripped')
        np.fill(arming)
        time.sleep(10)
        np.fill(armed)
        while not break_beam.value:
            np.fill(armed)
        
    
