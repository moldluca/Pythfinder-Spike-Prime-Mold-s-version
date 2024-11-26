from pybricks.hubs import PrimeHub

# generic class for message showcasing on brick's screen
class TelemetryEx():
    def __init__(self, brick: PrimeHub):
        self.__brick = brick
    
    def addData(self, *message):
        self.__brick.screen.print(message)
    
    def clear(self):
        self.__brick.screen.clear()
