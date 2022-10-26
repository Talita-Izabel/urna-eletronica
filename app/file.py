import json
import os 
from fileinput import filename


class File:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, 'r') as arquivo:
            texto = arquivo.readlines()
        return texto

    def write(self, texto):
        if os.path.exists(self.filename) == False: 
            open(self.filename, 'x')

        with open(self.filename, 'a') as arquivo:
            texto = texto + '\n'
            arquivo.write(texto)

    def readJSON(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)
            return data

    def clearFile(self):
        if os.path.exists(self.filename): 
            os.remove(self.filename)