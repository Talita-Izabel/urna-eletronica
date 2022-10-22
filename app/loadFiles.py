from file import File
from voter import Voter
from dictionaries import eleitores, deputadosEstadual, deputadosFederal, governadores, presidentes, senadores, countingOfVotes

class LoadFiles:
    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        self.fillDictionaries('eleitores.txt', eleitores)
        self.fillDictionaries('candidatos_deputado_estadual.txt', deputadosEstadual)
        self.fillDictionaries('candidatos_deputado_federal.txt', deputadosFederal)
        self.fillDictionaries('candidatos_governador.txt', governadores)
        self.fillDictionaries('candidatos_presidente.txt', presidentes)
        self.fillDictionaries('candidatos_senador.txt', senadores)

        print(eleitores.items())

        # Votos em branco e nulos
        countingOfVotes['blank'] = 0
        countingOfVotes['null'] = 0

    def fillDictionaries(self, file, dictionary) :
        url = (f'{self.path}/{file}')
        file = File(url)

        text = file.read()
        for line in text:
            name = line.split(',')[0]


            if(dictionary != eleitores):
                number = line.split(',')[1].removesuffix('\n').strip()
                countingOfVotes[name] = 0
                dictionary[number] = name

                print(name, number)
            else:
                number = line.split(',')[1].strip()
                section = line.split(',')[2].removesuffix('\n').strip()
                elector = Voter(name, number, section)
                dictionary[number] = elector
                print(name, number, section)
            
        print()

