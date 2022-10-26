import os
import jsonpickle
from candidate import Candidate
from file import File
from loadFiles import LoadFiles
from controlCenter import ControlCenter
from candidate import DEPUTADO_ESTADUAL, DEPUTADO_FEDERAL, GOVERNADOR, PRESIDENTE, SENADOR, Candidate
from dictionaries import eleitores, candidatos, listaVotos

class CountingVoutes:

    def initializesCount(self):
        load = LoadFiles('./data')
        
        load.fillDictionaries('eleitores.txt', eleitores, 9)
        load.fillDictionaries('candidatos_deputado_estadual.txt', candidatos, DEPUTADO_ESTADUAL)
        load.fillDictionaries('candidatos_deputado_federal.txt', candidatos, DEPUTADO_FEDERAL)
        load.fillDictionaries('candidatos_governador.txt', candidatos, GOVERNADOR)
        load.fillDictionaries('candidatos_presidente.txt', candidatos, PRESIDENTE)
        load.fillDictionaries('candidatos_senador.txt', candidatos, SENADOR)

        self.getFiles()

    def getFiles(self):
        path = './data/counting-votes'

        for diretorio, subpastas, arquivos in os.walk(path):
            for arquivo in arquivos:
                if(arquivo == 'report-card.txt'):
                    continue
                print(os.path.join(os.path.realpath(diretorio), arquivo))
                texto = ControlCenter().decryptFile(os.path.join(os.path.realpath(diretorio), arquivo))
                texto = texto.split('\n')

                for linha in texto:
                    # Verifica se não há linha vazia
                    if len(linha) == 0:
                        continue

                    decoded = jsonpickle.decode(linha)
                    classCandidate = decoded[1]

                    classCandidate.addVote(classCandidate.getVotes())

                    candidatos.update({ decoded[0]: classCandidate })

        self.separateCategories()

    def separateCategories(self):
        candidateDF = []
        candidateDE = []
        candidateG = []
        candidateS = []
        candidateP = []

        for i in candidatos.items():
            category = i[1].getOffice()

            if category == DEPUTADO_FEDERAL:
                candidateDF.append(i[1])
            elif category == DEPUTADO_ESTADUAL:
                candidateDE.append(i[1])
            elif category == GOVERNADOR:
                candidateG.append(i[1])
            elif category == SENADOR:
                candidateS.append(i[1])
            elif category == PRESIDENTE:
                candidateP.append(i[1])


        filename = './data/counting-votes/report-card.txt'
        if os.path.exists(filename): 
            os.remove(filename)

        self.generateReportCard('Deputado Federal', candidateDF)
        self.generateReportCard('Deputado Estadual', candidateDE)
        self.generateReportCard('Governador', candidateG)
        self.generateReportCard('Senador', candidateS)
        self.generateReportCard('Presidente', candidateP)



    def  generateReportCard(self, category, dictionary):
        filename = './data/counting-votes/report-card.txt'
        file = File(filename)

        file.write((f'\n\t - {category}'))

        for i in dictionary:
            line = (f'{i.getName()}\t\t\t\t{i.getNumber()}\t\t{i.getVotes()}')
            file.write(line)
        
        file.write('\n\n')

CountingVoutes().initializesCount()                