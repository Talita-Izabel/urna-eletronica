from dictionaries import eleitores, deputadosEstadual, deputadosFederal, governadores, presidentes, senadores, countingOfVotes

class Voting:

    def startVoting(self):
        while(True):
            voter = self.getVoter('72053981695')

            number = input('Deputado Federal: ')
            candidate = self.getCandidate(number, deputadosFederal)
            self.addVote(candidate)

            number = input('Deputado Estadual: ')
            candidate = self.getCandidate(number, deputadosEstadual)
            self.addVote(candidate)

            number = input('Senador: ')
            candidate = self.getCandidate(number, senadores)
            self.addVote(candidate)

            number = input('Governador: ')
            candidate = self.getCandidate(number, governadores)
            self.addVote(candidate)

            number = input('Presidente: ')
            candidate = self.getCandidate(number, presidentes)
            self.addVote(candidate)

    def getCandidate(self, number, dictionary):
        candidate = dictionary.get(number)
        if candidate == None or candidate == '#': 
            candidate = 'null' 
            print('\tNULO')
        elif candidate == '*': candidate = 'blank'
        else:
            print(f'\tCadidato: {candidate} - {number}')
        return candidate

    def getVoter(self, number):
        print(eleitores.get(number))
        return eleitores.get(number)

    def addVote(self, candidate):
        if candidate == None or candidate == '#': candidate = 'null'
        if candidate == '*': candidate = 'blank'

        value = countingOfVotes.get(candidate)
        countingOfVotes.update({candidate:value+1})
        # print(countingOfVotes.items())
        print()