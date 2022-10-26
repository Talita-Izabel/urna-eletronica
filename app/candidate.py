DEPUTADO_FEDERAL = 0
DEPUTADO_ESTADUAL = 1
SENADOR = 2
GOVERNADOR = 3
PRESIDENTE = 5

class Candidate():
        def __init__(self, name, number, office, votes):
            self.name = name
            self.number = number
            self.office = office
            self.votes = votes

        def getName(self):
            return self.name

        def getNumber(self):
            return self.number

        def getOffice(self):
            return self.office

        def getVotes(self):
            return self.votes

        def setVotes(self, votes):
            self.votes = votes