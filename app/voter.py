class Voter:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.voted = False

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def getVoted(self):
        return self.voted