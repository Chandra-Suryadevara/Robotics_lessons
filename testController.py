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

    def pretesting(self):
        joysticks = []
        for i in range(0, pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
            joysticks[-1].init()
        print(pygame.joystick.Joystick(0).get_name())


    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis < 2:
                        if event.axis == 0:  # left/right
                            if event.value < -0.5:
                                print("Left")
                                print(event.value)
                                speed = int(event.value * (-255))
                                byte_array = bytearray([1, 1, speed, 2, 0, speed, 3, 1, speed, 4, 0, speed])
                                self.communicator.write(byte_array)
                            elif event.value > 0.5:
                                print("Right")
                                print(event.value)
                                speed = int(event.value * 255)
                                byte_array = bytearray([1, 0, speed, 2, 1, speed, 3, 0, speed, 4, 1, speed])
                                self.communicator.write(byte_array)
                            else:
                                self.stop_all_motors()

                        if event.axis == 1:  # up/down
                            if event.value < -0.5:
                                print("Up")
                                print(event.value)
                                speed = int(event.value * (-255))
                                byte_array = bytearray([1, 1, speed, 2, 1, speed, 3, 1, speed, 4, 1, speed])
                                self.communicator.write(byte_array)
                            elif event.value > 0.5:
                                print("Down")
                                print(event.value)
                                speed = int(event.value * 255)
                                byte_array = bytearray([1, 0, speed, 2, 0, speed, 3, 0, speed, 4, 0, speed])
                                self.communicator.write(byte_array)
                            else:
                                self.stop_all_motors()

            # Add a delay to control input handling rate
            time.sleep(0.1)  # Delay in seconds (100 milliseconds)


c1 = Xbox_Controller_Robot()
c1.start_game()
