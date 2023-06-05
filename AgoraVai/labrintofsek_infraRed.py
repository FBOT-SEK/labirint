#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

ultrasonic_sensor_in2 = UltrasonicSensor(INPUT_2)
ultrasonic_sensor_in3 = UltrasonicSensor(INPUT_3)
infra_red_in5 = InfraredSensor(INPUT_1)
gyro_sensor_in4 = GyroSensor(INPUT_4)

#motorC = LargeMotor(OUTPUT_C) # Magnet
# Here is where your code starts
def mover():
    while infra_red_in5.distance_centimeters > 15:
        if gyro_sensor_in4.angle < 0:
            tank_drive.on(20,10)
        elif gyro_sensor_in4.angle > 0:
            tank_drive.on(10,20)
        else:
            tank_drive.on(20,20)
    tank_drive.off()

def direita():
    while gyro_sensor_in4.angle < 90:
        tank_drive.on(5,-5)
    tank_drive.off()
    gyro_sensor_in4.reset()
    
def esquerda():
    while gyro_sensor_in4.angle > -90:
        tank_drive.on(-5,5)
    tank_drive.off()
    gyro_sensor_in4.reset()

while True:
    mover()
    if ultrasonic_sensor_in2.distance_centimeters < ultrasonic_sensor_in3.distance_centimeters:
        direita()
    else:
        esquerda()