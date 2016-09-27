from machine import Pin
from Servo import Servo
import time

# base can rotate from 0 to 180 degrees centered at 90
# gear ratio causes range of motion to be about 90 degrees
rotate = Servo(Pin(4))
              
# right servo can rotate from 110 (back) to 180 (forward)
right_servo = Servo(Pin(13)) # forward/back
# back is right_servo.write_angle(110)
# front is right_servo.write_angle(180)

# left servo can rotate from 110 (down) to 180 (up)
left_servo = Servo(Pin(12)) # up/down

# gripper servo from 0 to 180
gripper = Servo(Pin(5))

# init to base positions
def init():
    gripper.write_angle(0)    
    right_servo.write_angle(110)
    left_servo.write_angle(120)
    rotate.write_angle(90)
    #gripper.write_angle(5)
    time.sleep(.5)
    gripper.write_us(0)    
    right_servo.write_us(0)
    left_servo.write_us(0)
    rotate.write_us(0)

# demo
def demo():
    rotate.write_angle(0)
    time.sleep(0.75)
    rotate.write_angle(180)
    time.sleep(1.2)
    rotate.write_angle(90)
    time.sleep(0.75)
    
    right_servo.write_angle(180)
    time.sleep(0.75)
    right_servo.write_angle(110)
    time.sleep(0.75)
    
    left_servo.write_angle(180)
    time.sleep(0.75)
    left_servo.write_angle(110)
    time.sleep(0.75)
    left_servo.write_angle(120)
    time.sleep(0.1)
    
    gripper.write_angle(120)
    time.sleep(0.5)
    gripper.write_angle(0)
    time.sleep(.5)
    gripper.write_angle(120)
    time.sleep(.5)
    gripper.write_angle(0)
    time.sleep(.5)
    gripper.write_angle(5)

def gocrazy():
    left_dir = True
    left = 110  
    right_dir = True                                                                                                                                      
    right = 110                                                                                                                                       
    gripper_dir = True
    gripper_angle = 0  
    rotate_angle = 0
    rotate_dir = True                                                                                                                              
    start = time.time()

    while time.time() - start < 5.0:
        left += 1 if left_dir else -1
        right += 1.1 if right_dir else -1.1
        gripper_angle += 2.45 if gripper_dir else -2.45
        rotate_angle += 2.45 if rotate_dir else -2.45
        if left > 180:
            left = 180
            left_dir = False
        if left < 110:
            left = 110
            left_dir = True
        if right > 180:
            right = 180
            right_dir = False
        if right < 110:
            right = 110
            right_dir = True
        if gripper_angle > 120:
            gripper_angle = 120
            gripper_dir = False
        if gripper_angle < 0:
            gripper_angle = 0
            gripper_dir = True
        if rotate_angle > 180:
            rotate_angle = 180
            rotate_dir = False
        if rotate_angle < 0:
            rotate_angle = 0
            rotate_dir = True
    
        time.sleep(0.01)
        left_servo.write_angle(int(left))
        right_servo.write_angle(int(right))
        gripper.write_angle(int(gripper_angle))
        rotate.write_angle(int(rotate_angle))

pressed = False

def button_pressed(pin):
    global pressed
    if not pressed:
        print("Pressed at", time.ticks_ms())
        pressed = True

def wait_for_button():
    global pressed
    mode = 0
    while True:
        if pressed:
            if mode == 0:
                demo()
            elif mode == 1:
                gocrazy()
            init()
            mode = (mode + 1) % 2
            pressed = False
        else:
            time.sleep(.5)

button = Pin(14, Pin.IN, Pin.PULL_UP)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

if button.value() == 0:
    # if button is held down on boot start infinite loop waiting for button
    wait_for_button()