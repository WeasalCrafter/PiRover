import pigpio
import os

pins = {
  "frontL": 15,
  "frontR": 14,
  "backL": 18,
  "backR":4
}

CW = 900
CCW = 1800

os.system('sudo pigpiod')

pi = pigpio.pi()
pi.set_mode(pins["backR"], pigpio.OUTPUT)
pi.set_mode(pins["backL"], pigpio.OUTPUT)
pi.set_mode(pins["frontR"], pigpio.OUTPUT)
pi.set_mode(pins["frontL"], pigpio.OUTPUT)

def forward():
    move(CW,CCW,CW,CCW)
def backward():
    move(CCW,CW,CCW,CW)
def left():
    move(CW,CW,CW,CW)
def right():
    move(CCW,CCW,CCW,CCW)

def move(frontR,frontL,backR,backL):
    pi.set_servo_pulsewidth(pins["backR"],backR)
    pi.set_servo_pulsewidth(pins["backL"],backL)
    pi.set_servo_pulsewidth(pins["frontR"],frontR)
    pi.set_servo_pulsewidth(pins["frontL"],frontL)

def sleep():
    for x in pins:
        pi.set_PWM_dutycycle(pins[x],0)
        pi.set_PWM_frequency(pins[x],0)
