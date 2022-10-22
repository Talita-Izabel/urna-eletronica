class Voter:

    def __init__(self, name, number, section):
        self.name = name
        self.number = number
        self.section = section
        self.voted = False

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def getSection(self):
        return self.section

    def getVoted(self):
        return self.voted

    def setVoted(self):
        self.voted = True