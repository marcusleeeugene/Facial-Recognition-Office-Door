''''
Real Time Face Recogition
    ==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc
    ==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition
Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18
'''

import cv2
import numpy as np
import os
import lcddriver
from time import *
import time
import RPi.GPIO as GPIO

PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
COUNTER = 0

def invoke():
    print("Start")
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(2.4)
    print("End")

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcus: id=1,  etc
names = ['None', 'Marcus', 'Zhi Cheng', 'Jun Yan', 'Hong Chai', 'Peng Hian', 'Yi Chou', 'Sophie']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 480) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#Set up LCD variable
lcd = lcddriver.lcd()

while True:
    GPIO.output(PIN, GPIO.HIGH)
    cam.grab()
    cam.grab()
    cam.grab()
    cam.grab()
    cam.grab()
    cam.grab()
    cam.grab()
    cam.grab()
    cam.grab()

    ret, img = cam.retrieve()
    #img = cv2.flip(img, -1) # Flip vertically
    img = rotateImage(img, 90)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Used to break out of while loops later on if face matches
    successflag = 0


    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        lcd.lcd_clear()
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100 and confidence < 70): #If actual confidence at least 20
            id = names[id]
            confidence = "  {0}%".format(round(100-confidence))
            print(id)
            lcd.lcd_display_string("Welcome, ", 1)
            lcd.lcd_display_string(id + "!", 2)
            invoke()
            successflag = 1
            break
        else:
            id = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence)) #if confidence 80, actual confidence 20
            print(id)
            lcd.lcd_display_string("Determining", 1)
            lcd.lcd_display_string("identity...", 2)

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

    #Break out of while loop then unlock door
    if (successflag == 1):
        print("\n [UNLOCKED]")
        lcd.lcd_clear()
        #break;

    cv2.imshow('camera',img)


    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
