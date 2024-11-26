from pybricks.parameters import Button
from pybricks.hubs import PrimeHub

from BetterClasses.EdgeDetectorEx import *


# edge detectors for each button on the brick


class ButtonEx:
    def __init__(self, brick: PrimeHub):
        self.__brick = brick

        # dictionary for all Spike Prime buttons (excepting the blothoot button, we don't talk about that)
        self.__buttons = {
            Button.LEFT: EdgeDetectorEx(), 
            Button.RIGHT: EdgeDetectorEx(), 
            Button.CENTER: EdgeDetectorEx()
        }

        self.__pressed_buttons = []

    def updateButtons(self):
        # get the current gamepad state
        self.__pressed_buttons = self.__brick.buttons.pressed()
        
        if not self.__pressed_buttons:
            # no button is pressed
            for detector in self.__buttons.values():
                detector.set(False)
                detector.update()
            
            return None
            
        # take only the first pressed button
        pressed_button = next(iter(self.__pressed_buttons))

        for button, detector in self.__buttons.items():
            if pressed_button == button:
                detector.set(True)
            else: detector.set(False)    
            detector.update()      



    def wasJustPressed(self, button: Button):
        try: 
            return self.__buttons[button].rising
        except: print("\n\nthat's not a button?? {0}".format(button))

    def wasJustReleased(self, button: Button):
        try:
            return self.__buttons[button].falling
        except: print("\n\nthat's not a button??")



    def isPressed(self, button: Button):
        try:
            return self.__buttons[button].high
        except: print("\n\nthat's not a button??")

    def isReleased(self, button: Button):
        try:
            return self.__buttons[button].low
        except: print("\n\nthat's not a button??")
