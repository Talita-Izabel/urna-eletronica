from voter import Voter
from dictionaries import eleitores, deputadosEstadual, deputadosFederal, governadores, presidentes, senadores, countingOfVotes

class Voting:

    def startVoting(self):
        while(True):
            number = input('Número eleitor: ')
            voter = self.getVoter(number)
            if voter == None: continue

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

            # Informa que o eleitor votou
            voter.setVoted()
            eleitores.update({voter.getNumber: voter})


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
        voter = eleitores.get(number)
        print('VOTER', voter.getName())
        # Verificar se o eleitor já votou.
        try:
            if voter == None:
                raise ValueError()

            if voter.getVoted() == True:
                raise NameError()
        except NameError:                
            print('Eleitor já votou!')
            return None
        except ValueError:                
            print('Eleitor não encontrado!')
            return None


        return voter

    def addVote(self, candidate):
        if candidate == None or candidate == '#': candidate = 'null'
        if candidate == '*': candidate = 'blank'

        value = countingOfVotes.get(candidate)
        countingOfVotes.update({candidate:value+1})
        # print(countingOfVotes.items())
        print()
