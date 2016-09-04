import sys
import logging
import zmq
import simplejson
import time
import math
import zmq
import time

from threading import Thread

from threading import Timer, Lock

context = zmq.Context()
kctrl_conn = context.socket(zmq.PUSH)
kctrl_conn.connect("tcp://127.0.0.1:5125")

while True :
    var = raw_input("Please enter something: ")
    print "you entered", var

    #do something
