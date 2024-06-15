class RemoteTv():
    # Initialize the TV with the switch off and brightness at 0
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    # Method to turn the TV on
    def turnOn(self):
        self.switchIsOn = True

    # Method to turn the TV off
    def turnOff(self):
        self.switchIsOn = False

    # Method to raise the brightness level, max brightness is 10
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    # Method to lower the brightness level, min brightness is 0
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging: shows the current state of the TV
    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)

# Main code
remoteSatu = RemoteTv()

# Turn switch on, and raise the brightness level 5 times
remoteSatu.turnOn()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.show()

# Lower the brightness level 2 times, and turn switch off
remoteSatu.lowerLevel()
remoteSatu.lowerLevel()
remoteSatu.turnOff()
remoteSatu.show()
