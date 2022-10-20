from dictionaries import eleitores, deputadosEstadual, deputadosFederal, governadores, presidentes, senadores

class Voting:

    def startVoting(self):
        self.getVoter('72053981695')

        number = input('Deputado Federal: ')
        self.getCandidate(number, deputadosFederal)

        number = input('Deputado Estadual: ')
        self.getCandidate(number, deputadosEstadual)

        number = input('Senador: ')
        self.getCandidate(number, senadores)

        number = input('Governador: ')
        self.getCandidate(number, governadores)

        number = input('Presidente: ')
        self.getCandidate(number, presidentes)

    def getCandidate(self, number, dictionary):
        print(dictionary.get(number))

    def getVoter(self, number):
        print(eleitores.get(number))