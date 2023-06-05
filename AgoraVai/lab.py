#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from threading import Thread
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
front_sensor = InfraredSensor(INPUT_1) 
left_sensor = UltrasonicSensor(INPUT_2) 
right_sensor = UltrasonicSensor(INPUT_3)  
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

# Here is where your code starts

def correction():
    if (right_sensor.distance_centimeters and left_sensor.distance_centimeters) > 25:
        tank_drive.on(20, 20)
    elif right_sensor.distance_centimeters < left_sensor.distance_centimeters:
        print("right_sensor.distance_centimeters > left_sensor.distance_centimeters")
        print("right sensor: ", right_sensor.distance_centimeters)
        print("left sensor: ", left_sensor.distance_centimeters)
        
        if right_sensor.distance_centimeters > 5 and right_sensor.distance_centimeters < 10:
            tank_drive.on(20, 17)
        elif right_sensor.distance_centimeters < 5:
            tank_drive.on(17, 20)
        else:
            tank_drive.on(20, 20)
    else:
        print("left_sensor.distance_centimeters > right_sensor.distance_centimeters")
        print("right sensor: ", right_sensor.distance_centimeters)
        print("left sensor: ", left_sensor.distance_centimeters)
        if left_sensor.distance_centimeters > 5 and left_sensor.distance_centimeters < 10:
            tank_drive.on(17, 20)
        elif left_sensor.distance_centimeters < 5:
            tank_drive.on(21, 15)
        else:
            tank_drive.on(20, 20)
        
        
"""def left_proximity(dist2follow):
    print(dist2follow)
    dist = int(left_sensor.distance_centimeters)
    if dist < dist2follow - 5 or dist > dist2follow + 5:
            dist2follow = dist
            # print("dist2follow = dist")
            # print(dist2follow)
            # print(dist)
    elif dist < dist2follow:
            tank_drive.on(18, 20)
            odometry.get_pos()
            # print(dist2follow)
            # print(dist)
            # print("dist < dist2follow")
    elif dist > dist2follow:
        tank_drive.on(20, 18)
        odometry.get_pos()
            # print(dist2follow)
            # print(dist)
            # print("dist > dist2follow")
    elif dist == dist2follow:
        tank_drive.on(20, 20)
        odometry.get_pos()
            # print(dist2follow)
            # print(dist)
            # print("dist == dist2follow")
    time.sleep(0.1)"""

def move_straight():
    dist2follow = int(right_sensor.distance_centimeters)
    while front_sensor.proximity > 12:
        correction()
        '''
        if front_sensor.proximity > 90 and left_sensor.distance_centimeters > 90 and right_sensor.distance_centimeters > 90:
            break
        '''
        # tank_drive.on(20, 20)
        odometry.get_pos()  # Atualiza a posição do robô
        # left_proximity()
        # right_proximity()
        # #finish()
    '''
    if front_sensor.proximity > 90 and left_sensor.distance_centimeters > 90 and right_sensor.distance_centimeters > 90:
        return True
    else:
        return False
    '''
    # tank_drive.off(brake=True)

def turn_left():
    gyro_sensor.reset()
    while gyro_sensor.angle > -89.5:
        tank_drive.on(-5, 5)
        odometry.get_pos()
        print(gyro_sensor.angle)
    tank_drive.off(brake=True)

def turn_right():
    gyro_sensor.reset()
    while gyro_sensor.angle < 86:
        tank_drive.on(5, -5)
        odometry.get_pos() 
        print(gyro_sensor.angle)
    tank_drive.off(brake=True)
    
while True:
    #odometry.log_pos()
    move_straight()
    if left_sensor.distance_centimeters > right_sensor.distance_centimeters:
        turn_left()
        print(right_sensor.distance_centimeters)
    else:
        turn_right()
        print(left_sensor.distance_centimeters)
    #finish()

tank_drive.off(brake=True)