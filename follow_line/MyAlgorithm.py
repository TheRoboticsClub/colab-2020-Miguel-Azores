#!/usr/bin/python
#-*- coding: utf-8 -*-
import threading
import time
from datetime import datetime

from simple_pid import PID
import math
import cv2
import numpy as np

time_cycle = 80
(w, h) = (640,240)
start_height_0 = h + 10
start_height_1 = h + 150

# define range of red color
low_red = np.array([100,0,0])
high_red = np.array([255,95,95])



class MyAlgorithm(threading.Thread):

    def __init__(self, camera, motors):
        self.camera = camera
        self.motors = motors
        self.threshold_image = np.zeros((640,360,3), np.uint8)
        self.color_image = np.zeros((640,360,3), np.uint8)
        self.stop_event = threading.Event()
        self.kill_event = threading.Event()
        self.lock = threading.Lock()
        self.threshold_image_lock = threading.Lock()
        self.color_image_lock = threading.Lock()
        threading.Thread.__init__(self, args=self.stop_event)

    def getImage(self):
        self.lock.acquire()
        img = self.camera.getImage().data
        self.lock.release()
        return img

    def set_color_image (self, image):
        img  = np.copy(image)
        if len(img.shape) == 2:
          img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        self.color_image_lock.acquire()
        self.color_image = img
        self.color_image_lock.release()

    def get_color_image (self):
        self.color_image_lock.acquire()
        img = np.copy(self.color_image)
        self.color_image_lock.release()
        return img

    def set_threshold_image (self, image):
        img = np.copy(image)
        if len(img.shape) == 2:
          img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        self.threshold_image_lock.acquire()
        self.threshold_image = img
        self.threshold_image_lock.release()

    def get_threshold_image (self):
        self.threshold_image_lock.acquire()
        img  = np.copy(self.threshold_image)
        self.threshold_image_lock.release()
        return img

    def run (self):

        while (not self.kill_event.is_set()):
            start_time = datetime.now()
            if not self.stop_event.is_set():
                self.algorithm()
            finish_Time = datetime.now()
            dt = finish_Time - start_time
            ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
            #print (ms)
            if (ms < time_cycle):
                time.sleep((time_cycle - ms) / 1000.0)

    def stop (self):
        self.stop_event.set()

    def play (self):
        if self.is_alive():
            self.stop_event.clear()
        else:
            self.start()

    def kill (self):
        self.kill_event.set()

    def drawLines (self, image):
        cv2.line(image,(300, 0),(300, 500),(255,150,0),2)
        cv2.line(image,(260, 0),(260, 500),(255,0,0),2)
        cv2.line(image,(200, 0),(200, 500),(255,0,255),2)
        cv2.line(image,(340, 0),(340, 500),(255,150,0),2)
        cv2.line(image,(400, 0),(400, 500),(255,0,0),2)
        cv2.line(image,(440, 0),(440, 500),(255,0,255),2)


    def algorithm(self):
        #GETTING THE IMAGES
        image = self.getImage()

        # Add your code here
        print "Runing time"

        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(image, low_red, high_red)

        # convert the grayscale image to binary image
        thresh = cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        signed_thresh_0 = thresh[start_height_0].astype(np.int16)
        signed_thresh_1 = thresh[start_height_1].astype(np.int16)
        diff_0 = np.diff(signed_thresh_0)
        diff_1 = np.diff(signed_thresh_1)
        points_0 = np.where(np.logical_or(diff_0 > 200, diff_0 < -200))
        points_1 = np.where(np.logical_or(diff_1 > 0, diff_1 < -200))

        cv2.line(image,(0,start_height_0),(640,start_height_0),(0,255,0),8)
        cv2.line(image,(0,start_height_1),(640,start_height_1),(0,255,0),8)

        if len(points_0) > 0 and len(points_0[0]) > 1: # if finds something like a black line
            print "HOLAA"
            middle_0 = (points_0[0][0] + points_0[0][-1]) / 2
            print middle_0
            cv2.circle(image, (middle_0, start_height_0), 5, (0,0,255), -1)

        if len(points_1) > 0 and len(points_1[0]) > 1: # if finds something like a black line
            print "HOLA 2"
            print len(points_1)
            middle_1 = (points_1[0][0] + points_1[0][-1]) / 2
            print middle_1
            cv2.circle(image, (points_1[0][0], start_height_1), 5, (255,0,0), -1)
            cv2.circle(image, (points_1[0][-1], start_height_1), 5, (255,0,255), -1)
            cv2.circle(image, (middle_1, start_height_1), 5, (0,0,255), -1)
            self.drawLines(image)

        # print cX
        if (middle_0 < 300):
            print "poquito derecha"
            self.motors.sendV(4.5)
            self.motors.sendW(0.03)
            if(middle_0 < 260):
                print "DERECHA"
                self.motors.sendV(3.2)
                self.motors.sendW(0.35)
                if(middle_0 < 200):
                	self.motors.sendV(3)
                	self.motors.sendW(1)

        elif (middle_0 > 340):
            print "poquito izquierda"
            self.motors.sendV(4.5)
            self.motors.sendW(-0.03)
            if (middle_0 > 400):
                print "IZQUIERDA"
                self.motors.sendV(3.2)
                self.motors.sendW(-0.35)
                if(middle_0 > 440):
                	self.motors.sendV(3)
                	self.motors.sendW(-1)
        else:
            self.motors.sendV(5)

        if (middle_1 < 300):
            print "    poquito derecha"
            self.motors.sendV(4.5)
            self.motors.sendW(0.03)
            if(middle_1 < 260):
                print "    DERECHA"
                self.motors.sendV(3.2)
                self.motors.sendW(0.35)
                if(middle_1 < 200):
                	print "    MAX DERECHA"
                	self.motors.sendV(3)
                	self.motors.sendW(1)

        elif (middle_1 > 340):
            print "    poquito izquierda"
            self.motors.sendV(4.5)
            self.motors.sendW(-0.03)
            if (middle_1 > 400):
                print "    IZQUIERDA"
                self.motors.sendV(3.2)
                self.motors.sendW(-0.35)
                if(middle_1 > 440):
                	print "    MAX IZQUIERDA"
                	self.motors.sendV(3)
                	self.motors.sendW(-1)
        else:
            self.motors.sendV(5)

        self.set_threshold_image(mask)
