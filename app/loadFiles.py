from file import File
from dictionaries import eleitores, deputadosEstadual, deputadosFederal, governadores, presidentes, senadores

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


    def fillDictionaries(self, file, dictionary) :
        url = (f'{self.path}/{file}')
        file = File(url)

        text = file.read()
        for line in text:
            name = line.split(',')[0]
            number = line.split(',')[1].removesuffix('\n')

            dictionary[name] = number

        print(dictionary.items())
        print()

