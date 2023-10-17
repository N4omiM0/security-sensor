buttonArm = dio.DigitalInOut(board.D3)
buttonArm.direction = dio.Direction.INPUT
buttonDisarm = dio.DigitalInOut(board.D4)
buttonDisarm.direction = dio.Direction.INPUT

armed = False

def arm():
    global armed
    np.fill(BLACK)
    np.show()
    time.sleep(0.5)
    np.fill(YELLOW)
    np.show()
    time.sleep(10)
    np.fill(RED)
    np.show()
    armed = True
    print(armed)

def disarm():
    global armed
    np.fill(GREEN)
    np.show()
    armed = False
    print(armed)

while True:
    if buttonArm.value == False:
        arm()
    if buttonDisarm.value == False:
        disarm()
