import ast
import os
import jsonpickle
import gnupg
import random
from file import File
from unicodedata import normalize
from dictionaries import listaVotos

path = os.getcwd() + "/app/config/env.json"    
env = File(path).readJSON()

class ControlCenter:

    def __init__(self):
        path = os.getcwd() + "/app/config/env.json"
        env = File(path).readJSON()
        gpg = gnupg.GPG(gnupghome=env['gnupghome'])
        gpg.encoding = 'utf-8'

        self.gpg = gpg

    def signVote(self, name, number, votes):
        print('Sign vote')

        # Transforma o objeto em string
        votes = { 'name': name, 'number': number, 'votes': votes }

        serialized = str(votes)

        key = self.getVoterKey(name)

        # Assina a com a chave do eleitor
        signedData = self.gpg.sign(serialized, keyid=key['fingerprint'], passphrase=env['password'])
        #print('Chave eleitor', signedData)

        signedStr = jsonpickle.encode(signedData)

        # Assina a com a chave do mesario
        key = self.getPrivKey('mesario')

        signedData = self.gpg.sign(signedStr, keyid=key['fingerprint'], passphrase=env['password'])
        #print('Chave mesario', signedData)

        signedStr = jsonpickle.encode(signedData)
        #print(type(signedStr), signedStr)

        # Adiciona string final do voto na lista (para não ir sempre no arquivo)
        listaVotos.append(signedStr)

        # Embaralha a lista
        random.shuffle(listaVotos) 

        url = './data/votos_eleitores.txt'
        file = File(url)

        file.clearFile()
        for vote in listaVotos:
            file.write(vote)

        # Após salvar no arquivo a urna irá encriptar o arquivo
        # key = self.getPrivKey('urna')
        # key_tse = self.getPrivKey('tse')
        # encrypted_ascii_data = self.gpg.encrypt_file(open(url, 'rb'), key_tse['fingerprint'], passphrase=env['password'])
        # print(encrypted_ascii_data, type(encrypted_ascii_data))



        # # Transforma em sign novamente
        # teste = jsonpickle.decode(signedStr)

        # decrypted = self.gpg.decrypt(message=teste.data, passphrase=env['password'])
        # #print('\n\n',decrypted.data, type(decrypted))

        # teste = jsonpickle.decode(decrypted.data)
        # #print(teste.data, type(teste))


        # # Repete
        # signedStr = jsonpickle.encode(teste)
        # teste = jsonpickle.decode(signedStr)
        # decrypted = str(self.gpg.decrypt(message=teste.data, passphrase=env['password']))
        # print('\n\n',decrypted, type(decrypted))

        # dict = ast.literal_eval(decrypted)
        # print(dict, type(dict))   

    def getVoterKey(self, voterName):
        print(voterName)

        nameFile = voterName.replace(' ', '-').lower()
        nameFile = normalize('NFKD', nameFile).encode('ASCII','ignore').decode('ASCII')
        
        privPath = '/home/talita/Documentos/TSI/6_Periodo/seguranca/trabalho/keys/priv' + '/priv-' + nameFile + '.pem'
        print(privPath)

        key = self.gpg.scan_keys(privPath)

        print(key[0]['fingerprint'])
        
        return key[0]

    def getPrivKey(self, name):
        privPath = '/home/talita/Documentos/TSI/6_Periodo/seguranca/trabalho/keys/priv' + '/priv-' + name + '.pem'
        key = self.gpg.scan_keys(privPath)

        return key[0]

    def decryptVote(self, voteStr):
        # Transforma em sign novamente
        teste = jsonpickle.decode(voteStr)

        decrypted = self.gpg.decrypt(message=teste.data, passphrase=env['password'])
        #print('\n\n',decrypted.data, type(decrypted))

        teste = jsonpickle.decode(decrypted.data)
        #print(teste.data, type(teste))


        # Repete
        signedStr = jsonpickle.encode(teste)
        teste = jsonpickle.decode(signedStr)
        decrypted = str(self.gpg.decrypt(message=teste.data, passphrase=env['password']))
        #print('\n\n',decrypted, type(decrypted))

        dict = ast.literal_eval(decrypted)
        #print(dict, type(dict))   
        return dict

    # Caso precise para validar os votos e eleitores
    def decryptVotersVoteFile(self):
        url = './data/votos_eleitores.txt'
        with open(url, 'r') as arquivo:
            texto = arquivo.read()

        texto = texto.split('\n')
        for linha in texto:
            dictionary = self.decryptVote(linha)
            print(dictionary)
