#!/usr/bin/env python3

import serial
import time
import pygame
from time import sleep
from pygame.constants import JOYBUTTONDOWN
pygame.init()

class Xbox_Controller_Robot:

    def __init__(self):
        
        self.communicator = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.reset_input_buffer()
        self.pretesting()

    def reset_input_buffer(self):
        self.communicator.reset_input_buffer()

    def stop_all_motors(self):
        byte_array = bytearray([1,1,0,2,1,0,3,1,0,4,1,0])
        self.communicator.write(byte_array)



    def take_action(self, direction_number, speed):
        if direction_number == 1: #Forward Drive
            byte_array = bytearray([1,1,speed,2,1,speed,3,1,speed,4,1,speed])
            self.communicator.write(byte_array)
            time.sleep(1)
            self.stop_all_motors()
        if direction_number == 2: # Backward Drive
            byte_array = bytearray([1,0,speed,2,0,speed,3,0,speed,4,0,speed])
            self.communicator.write(byte_array)
            time.sleep(1)
            self.stop_all_motors()
        if direction_number == 3:#left drive (please figure out what we are doing)
            byte_array = bytearray([1,1,speed,2,1,speed,3,1,speed,4,1,speed])
            self.communicator.write(byte_array)
            time.sleep(1)
            self.stop_all_motors()
        if direction_number == 4:#right drive (please figure out what we are doing)
            byte_array = bytearray([1,1,speed,2,1,speed,3,1,speed,4,1,speed])
            self.communicator.write(byte_array)
            time.sleep(1)
            self.stop_all_motors()


    def pretesting(self):
        joysticks = []
        for i in range(0, pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
            joysticks[-1].init()
        print(pygame.joystick.Joystick(0).get_name())


    def start_game(self):
        while True or KeyboardInterrupt:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:

                    if event.axis < 2:
                        print(event.value)
                        #motor_speed = event.value * -1
                        #print(f"motor_speed: {motor_speed}")
                        if event.axis == 0: # left/right
                            if event.value < -0.5:
                                print("left")

                            if event.value > 0.5:
                                print("right")                        

                        if event.axis == 1: # up/down
                            if event.value < -0.5:
                                print("up")
                                
                            if event.value > 0.5:
                                print("down")

                    if event.axis > 2:
                        if event.axis==4:
                                print("Right Trigger") #Vlaue rnage from -1 to 1
                                print(event.value)

                        if event.axis==5:
                                print("Left Trigger") #Vlaue rnage from -1 to 1
                                print(event.value)




c1 = Xbox_Controller_Robot()
c1.start_game()



 #  while True:

        # Pack the numbers into a single byte array
  #      byte_array = bytearray(straightSpeed)

        # Send the entire byte array at once
   #     ser.write(byte_array)
        
     #   line = ser.readline().decode('utf-8').rstrip()
    #    print(line)
      #  time.sleep(1)




