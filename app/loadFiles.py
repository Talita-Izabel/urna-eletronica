from candidate import DEPUTADO_ESTADUAL, DEPUTADO_FEDERAL, GOVERNADOR, PRESIDENTE, SENADOR, Candidate
from file import File
from voter import Voter
from dictionaries import eleitores, candidatos

class LoadFiles:
    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        self.fillDictionaries('eleitores.txt', eleitores, 0)
        self.fillDictionaries('candidatos_deputado_estadual.txt', candidatos, DEPUTADO_ESTADUAL)
        self.fillDictionaries('candidatos_deputado_federal.txt', candidatos, DEPUTADO_FEDERAL)
        self.fillDictionaries('candidatos_governador.txt', candidatos, GOVERNADOR)
        self.fillDictionaries('candidatos_presidente.txt', candidatos, PRESIDENTE)
        self.fillDictionaries('candidatos_senador.txt', candidatos, SENADOR)

        print(eleitores.items())

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

                print(name, number)
            else:
                number = line.split(',')[1].strip()
                section = line.split(',')[2].removesuffix('\n').strip()
                elector = Voter(name, number, section)
                dictionary[number] = elector
                print(name, number, section)
            
        print()

