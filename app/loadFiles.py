from curses.ascii import isblank
import os
from controlCenter import ControlCenter 
from candidate import DEPUTADO_ESTADUAL, DEPUTADO_FEDERAL, GOVERNADOR, PRESIDENTE, SENADOR, Candidate
from file import File
from voter import Voter
from dictionaries import eleitores, candidatos, listaVotos

class LoadFiles:
    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        self.fillDictionaries('eleitores.txt', eleitores, 9)
        self.fillDictionaries('candidatos_deputado_estadual.txt', candidatos, DEPUTADO_ESTADUAL)
        self.fillDictionaries('candidatos_deputado_federal.txt', candidatos, DEPUTADO_FEDERAL)
        self.fillDictionaries('candidatos_governador.txt', candidatos, GOVERNADOR)
        self.fillDictionaries('candidatos_presidente.txt', candidatos, PRESIDENTE)
        self.fillDictionaries('candidatos_senador.txt', candidatos, SENADOR)

        self.loadVotes()

        # Votos em branco e nulos
        candidate = Candidate('blank', '#', None, 0)
        candidatos['blank'] = candidate

        candidate = Candidate('null', '*', None, 0)
        candidatos['null'] = candidate

    def fillDictionaries(self, file, dictionary, office) :
        url = (f'{self.path}/{file}')
        file = File(url)

        text = file.read()
        for line in text:
            name = line.split(',')[0]


            if(dictionary != eleitores):
                number = line.split(',')[1].removesuffix('\n').strip()

                candidate = Candidate(name, number, office, 0)

                dictionary[number] = candidate

    
            else:
                number = line.split(',')[1].strip()
                section = line.split(',')[2].removesuffix('\n').strip()
                elector = Voter(name, number, section)
                dictionary[number] = elector
    
    def loadVotes(self): 
        url = './data/votos_eleitores.txt'

        # Se o arquivo existir carrega os dados para a lista
        if os.path.exists(url): 
            url = './data/votos_eleitores.txt'
            with open(url, 'r') as arquivo:
                texto = arquivo.read()

            texto = texto.split('\n')
            for linha in texto:
                # Verifica se não há linha vazia
                if len(linha) == 0:
                    continue
                listaVotos.append(linha)
                dictionary = ControlCenter().decryptVote(linha)

                number = dictionary['number']

                voter = eleitores.get(number)

                voter.setVoted()
                eleitores.update({number: voter})

