#! /usr/bin/env python

import time
import os
import yaml
import jenkinsapi

import RPi.GPIO as GPIO
from jenkinsapi.jenkins import Jenkins

client = None
config = None
ledA = 14
switchA = 15
ledB = 23
switchB = 24
armedButton = 17

def setup():
    load_config()
    setup_client()
    setup_pins()

def setup_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledA, GPIO.OUT)
    GPIO.setup(ledB, GPIO.OUT)
    GPIO.output(ledA, GPIO.HIGH)
    GPIO.output(ledB, GPIO.HIGH)
    GPIO.setup(switchA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(switchB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(armedButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def load_config():
    global config
    filepath = os.path.dirname(os.path.abspath(__file__))+ '/jenkins.yml'
    with open(filepath) as infile:
        config = yaml.load(infile)

def setup_client():
    global client
    while True:
        try:
            client = Jenkins(
                config['url'],
                config['user'],
                config['token'],
                ssl_verify=config['ssl_verify']
            )
            break
        except Exception as e:
            print "error: %s" % e
            time.sleep(5)

def toggle(pin):
    time.sleep(0.05)
    value = GPIO.input(pin)
    if pin == 15:
        GPIO.output(ledA, value)
    elif pin == 24:
        GPIO.output(ledB, value)

def engage(pin):
    time.sleep(0.05)
    if (not GPIO.input(ledA)) and (not GPIO.input(ledB)):
        print "engage!"
        GPIO.output(ledA, True)
        GPIO.output(ledB, True)
        client.build_job(config['job_name'])
    else:
        print "warming up..."

def loop():
    GPIO.add_event_detect(switchA, GPIO.RISING, callback=toggle, bouncetime=200)
    GPIO.add_event_detect(switchB, GPIO.RISING, callback=toggle, bouncetime=200)
    GPIO.add_event_detect(armedButton, GPIO.RISING, callback=engage, bouncetime=200)
    while True:
        pass

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    finally:
        destroy()

