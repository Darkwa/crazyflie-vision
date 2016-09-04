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


def new_value(value, targeted_value, step):
    if targeted_value > value:
        value = value + step
        if targeted_value < value:
            return targeted_value
    elif targeted_value < value:
        value = value - step
        if targeted_value > value:
            return targeted_value
    return value

sp_cmd = {
    "version": 1,
    "position": {
        "x": 0,
        "y": 0,
        "z": 0,
    }
}

axe = 0
x = 0.0
y = 0.0
z = 0.0
time_stamp = time.clock()

context = zmq.Context()
kctrl_conn = context.socket(zmq.PUSH)
kctrl_conn.connect("tcp://127.0.0.1:5125")
# TODO : must be multithreaded !
while True :
    var = raw_input("Please select the axe you want to change (x, y, z): ")
    if var == "x":
        axe = 1
        print"You've selected axe x"
    elif var == "y":
        print"You've selected axe y"
        axe = 2
    elif var == "z":
        print"You've selected axe z"
        axe = 3
    else:
        axe = 0
        print "Wrong value"

    #TODO add the previous value with a conditional string
    print "You selected "+var+". Previous value : %s"
    var = raw_input("Please enter the new value")
    try:
        var = float(var)
    except Exception :
        print "Wrong value"
        break

    time_stamp = time.clock()
    if axe == 1:
        while x != var:
            x = new_value(x, var, 1)
            print "target : {} ; value : {}".format(var, x)
            time.sleep(1)
    elif axe == 2:
        while y != var:
            y = new_value(y, var, 1)
            print "target : {} ; value : {}".format(var, y)
            time.sleep(1)
    elif axe == 3:
        while z != var:
            z = new_value(z, var, 1)
            print "target : {} ; value : {}".format(var, z)
            time.sleep(1)
    else:
        print "huh?"
    sp_cmd["position"]["x"] = x
    sp_cmd["position"]["y"] = y
    sp_cmd["position"]["z"] = z
    kctrl_conn.send_json(sp_cmd)


