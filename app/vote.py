class Vote:        
    def __init__(self, name, number, votes):
        self.name = name
        self.number = number
        self.votes = votes

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def getVotes(self):
        return self.votes