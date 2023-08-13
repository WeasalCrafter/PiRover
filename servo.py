import sys
import time
import tty
import termios
import os
os.system('sudo pigpiod')
import pigpio
print("servos started")

#filedescriptors = termios.tcgetattr(sys.stdin)
#tty.setcbreak(sys.stdin)
x = 0

backR = 15
backL = 14
frontR = 18
frontL = 4

CW = 900
CCW = 1800

pi = pigpio.pi()

pi.set_mode(backR, pigpio.OUTPUT)
pi.set_mode(backL, pigpio.OUTPUT)
pi.set_mode(frontR, pigpio.OUTPUT)
pi.set_mode(frontL, pigpio.OUTPUT)

def forward():
    pi.set_servo_pulsewidth(backR,CW)
    pi.set_servo_pulsewidth(backL,CCW)
    pi.set_servo_pulsewidth(frontR,CW)
    pi.set_servo_pulsewidth(frontL,CCW)
def backward():
    pi.set_servo_pulsewidth(backR,CCW)
    pi.set_servo_pulsewidth(backL,CW)
    pi.set_servo_pulsewidth(frontR,CCW)
    pi.set_servo_pulsewidth(frontL,CW)
def left():
    pi.set_servo_pulsewidth(backR,CW)
    pi.set_servo_pulsewidth(backL,CW)
    pi.set_servo_pulsewidth(frontR,CW)
    pi.set_servo_pulsewidth(frontL,CW)
def right():
    pi.set_servo_pulsewidth(backR,CCW)
    pi.set_servo_pulsewidth(backL,CCW)
    pi.set_servo_pulsewidth(frontR,CCW)
    pi.set_servo_pulsewidth(frontL,CCW)
def sleep():
    pi.set_PWM_dutycycle(backR,0)
    pi.set_PWM_frequency(backR,0)
    pi.set_PWM_dutycycle(backL,0)
    pi.set_PWM_frequency(backL,0)
    pi.set_PWM_dutycycle(frontR,0)
    pi.set_PWM_frequency(frontR,0)
    pi.set_PWM_dutycycle(frontL,0)
    pi.set_PWM_frequency(frontL,0)

try:
    while True:
        x = sys.stdin.read(1)[0]
        if x == "w" or x == "W":
            forward()
        if x == "s" or x == "S":
            backward()
        if x == "a" or x == "A":
            left()
        if x == "d" or x == "D":
            right()
        if x == "e" or x == "E":
            sleep()
except KeyboardInterrupt:
#    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)
    pi.stop()
    os.system('sudo killall pigpiod')
