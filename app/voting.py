from controlCenter import ControlCenter
from vote import Vote
from voter import Voter
from dictionaries import eleitores, candidatos
from candidate import DEPUTADO_ESTADUAL, DEPUTADO_FEDERAL, GOVERNADOR, PRESIDENTE, SENADOR

class Voting:

    def startVoting(self):
        while(True):
            votes = []

            number = input('Número eleitor: ')
            voter = self.getVoter(number)
            if voter == None: continue

            number = input('Deputado Federal: ')
            candidate = self.getCandidate(number, DEPUTADO_FEDERAL)
            self.addVote(candidate)
            votes.append(candidate.getNumber())

            number = input('Deputado Estadual: ')
            candidate = self.getCandidate(number, DEPUTADO_ESTADUAL)
            self.addVote(candidate)
            votes.append(candidate.getNumber())

            number = input('Senador: ')
            candidate = self.getCandidate(number, SENADOR)
            self.addVote(candidate)
            votes.append(candidate.getNumber())

            number = input('Governador: ')
            candidate = self.getCandidate(number, GOVERNADOR)
            self.addVote(candidate)
            votes.append(candidate.getNumber())

            number = input('Presidente: ')
            candidate = self.getCandidate(number, PRESIDENTE)
            self.addVote(candidate)
            votes.append(candidate.getNumber())


            # Gerenciar voto
            self.manageVote(voter, votes)

            # Informa que o eleitor votou
            voter.setVoted()
            eleitores.update({voter.getNumber(): voter})


    def getCandidate(self, number, office):
        candidate = candidatos.get(number)
        print(candidate)
        if candidate == None or candidate.getNumber() == '#' or candidate.getOffice() != office: 
            candidate = candidatos.get('null')
            print(candidate.getName(), candidate.getVotes())
            print('\tNULO')
        elif candidate.getNumber() == '*': candidate = candidatos.get('blank')
        else:
            print(f'\tCadidato: {candidate.getName()} - {number}')
        return candidate

    def getVoter(self, number):
        voter = eleitores.get(number)
        #print('VOTER', voter.getName())
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
        votes = candidate.getVotes() + 1
        candidate.setVotes(votes)

        candidatos.update({candidate.getNumber():candidate})
        print(candidatos.get(candidate.getNumber()).getName())
        print(candidatos.get(candidate.getNumber()).getVotes())
        print()

    def manageVote(self, voter, votes):
        name = voter.getName()
        number = voter.getNumber()

        #vote = Vote(name, number, votes)
        ControlCenter().signVote(name, number, votes)
