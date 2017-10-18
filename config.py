""" 
CAR CONFIG 

This file is read by your car application's manage.py script to change the car
performance. 

EXMAPLE
-----------
import dk
cfg = dk.load_config(config_path='~/d2/config.py')
print(cfg.CAMERA_RESOLUTION)

"""


import os

#PATHS
CAR_PATH = PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(CAR_PATH, 'data')
MODELS_PATH = os.path.join(CAR_PATH, 'models')

#VEHICLE
DRIVE_LOOP_HZ = 20
MAX_LOOPS = None

#CAMERA
CAMERA_RESOLUTION = (160, 120)
CAMERA_FRAMERATE = DRIVE_LOOP_HZ

#STEERING
STEERING_CHANNEL = 1
STEERING_LEFT_PWM = 460
STEERING_RIGHT_PWM = 307

#THROTTLE
THROTTLE_CHANNEL = 0
THROTTLE_FORWARD_PWM = 500
THROTTLE_STOPPED_PWM = 370
THROTTLE_REVERSE_PWM = 220

#TRAINING
BATCH_SIZE = 512
TRAIN_TEST_SPLIT = 0.8

#JOYSTICK
JOYSTICK_MAX_THROTTLE=1
JOYSTICK_STEERING_SCALE=1
USE_JOYSTICK_AS_DEFAULT=True
AUTO_RECORD_ON_THROTTLE=False

#ROTARY ENCODER
ROTARY_ENCODER_MM_PER_TICK=0.306096
ROTARY_ENCODER_PIN=4
MAX_VELOCITY=7.0

#THROTTLE PID
THROTTLE_PID_P=1.0
THROTTLE_PID_D=0.3
THROTTLE_PID_I=0.2

#LED INDICATOR PINS
RECORDING_LED=17

#LOG TO CONSOLE
DEBUG = True
