#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from odometry import Odometry
from time import sleep

# Create the sensors and motors objects
odometry = Odometry(OUTPUT_A, OUTPUT_B, 6.7, 23.8, 360, 360, debug=True)
gyro_sensor = GyroSensor(INPUT_4)
infra_red_in1 = InfraredSensor(INPUT_1) 
ultrasonic_sensor_in3 = UltrasonicSensor(INPUT_2) 
ultrasonic_sensor_in4 = UltrasonicSensor(INPUT_3)  
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

# Here is where your code starts
def move_straight():
    while infra_red_in1.proximity > 16:
        tank_drive.on(20, 20)
        odometry.get_pos()  # Atualiza a posição do robô
    tank_drive.off(brake=True)

def turn_left():
    gyro_sensor.reset()
    while gyro_sensor.angle > -90:
        tank_drive.on(-5, 5)
        odometry.get_pos() 
    tank_drive.off(brake=True)

def turn_right():
    gyro_sensor.reset()
    while gyro_sensor.angle < 90:
        tank_drive.on(5, -5)
        odometry.get_pos()  
    tank_drive.off(brake=True)

while True:
    #odometry.log_pos()
    move_straight()
    if ultrasonic_sensor_in3.distance_centimeters > ultrasonic_sensor_in4.distance_centimeters:
        turn_left()
    else:
        turn_right()

