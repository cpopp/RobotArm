# Robotic Arm with ESP8266 and MicroPython

The repository holds some basic code to drive a [3D printed robotic arm](https://www.thingiverse.com/thing:1454048) using an ESP8266 running [MicroPython firmware](https://micropython.org/download/#esp8266).  The included script waits for a button press and then runs the robotic arm through one of two movement sequences demonstrating its range of motion.

Check out a [video here](https://youtu.be/bKqB43CTn60).  

## Wiring
The robotic arm has four servos.  One for the gripper, one on the left for primarily vertical motion, one on the right for forward movement, and one in the base to handle rotation.

The signal wire from each servo hooks up to the ESP8266 as follows:

    Gripper: GPIO5
    Rotation: GPIO4
    Left Servo: GPIO12
    Right Servo: GPIO13

the button needs to be hooked up to ground and GPIO14.

## Code Setup

Place main.py from this repository and [servo.py](https://bitbucket.org/thesheep/micropython-servo/src) on the ESP8266.

## Startup

Hold the button, restart the ESP8266, and then release the button after a few seconds.  Pressing the button should result in the arm going through one of the two sequences of movements from the script.
