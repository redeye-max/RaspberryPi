#!/usr/bin/python3
import argparse
import RPi.GPIO as GPIO
import time

def setup(pin):
    GPIO.setmode(GPIO.BOARD)  # Use the numbering from the board
    GPIO.setwarnings(False)   # Do not warn if the pin is already set
    GPIO.setup(pin, GPIO.OUT)  # set the pin in output mode


def run(pin, value):
    if value is not 0:
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)



def main():
    parser = argparse.ArgumentParser(description='GPIO OUTPUT ON/OFF ')
    parser.add_argument('-p','--pin_num', type=int, help='GPIO pin number on board')
    parser.add_argument('-o','--output', type=int, help='0/1')

    args = parser.parse_args()

    if args.pin_num > 40 : 
        print('There are only 40 pins. Enter a number below 40') # No error check for valid pin
        exit(0)

    setup(args.pin_num)

    #TODO: Write a while loop here to turn led on and off
    # What do you see when the off duration is slowly increased
    #While loop
    #   turn on using run(args.pin_num, 1)
    #   sleep time.sleep(1/30.0)
    #   turn off     run(args.pin_num, 0)
    #   sleep    time.sleep(1/30.0) <---- tune this and see the effect. Lets discuss in next class

    run(args.pin_num, args.output)


if __name__ == '__main__': main()