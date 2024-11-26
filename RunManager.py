
from pybricks.tools import wait

from Controllers.RunController import *
from BetterClasses.ButtonsEx import *
from BetterClasses.MathEx import * 
from Trajectory.builder import *
from Settings.constants import *
from robot import *


# create the main robot object here
# set gyro orientation in **constants.py** if needed
core = Robot()

trajectory0 = (Trajectory()
               .read('run0'))

trajectory1 = (Trajectory()
               .read('run1'))

trajectory2 = (Trajectory()
               .read('run2'))



# you can create custom BEFORE / AFTER run functions
def start_run():
    global core

    if zeroBeforeEveryRun:
        core.zero()

def stop_run():
    ...



# create functions for each run you want to do
def run1():
    trajectory1.follow(core)

def run2():
    trajectory2.follow(core)

def run3():
    return 0

def run4():
    return 0

def run5():
    return 0

def run6():
    return 0

def run7():
    return 0

def dummy():
    wait(1000)

def test():
    trajectory0.follow(core)




# create a list of ---Run--- objects, binded to a button (NOT ---Button.CENTER---), giving a function
#         and optional ---one_time_use--- and  ---with_center---- combination
run_list = [Run(Button.LEFT, function = test, one_time_use = False)]

# MANDATORY!!! add a run list to the run controller from the robot class
#               otherwise, you'll get an error
core.run_control.addRunList(run_list)

# add before / after every run functions if you want
core.run_control.addBeforeEveryRun(function = start_run)
core.run_control.addAfterEveryRun(function = stop_run)

