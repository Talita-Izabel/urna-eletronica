from fileinput import filename


class File:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, 'r') as arquivo:
            texto = arquivo.readlines()
        return texto

    def write(self, texto):
        with open(self.filename, 'a') as arquivo:
            texto = '\n'+texto
            arquivo.write(texto)