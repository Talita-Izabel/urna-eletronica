import gnupg
from file import File

class KeyGeneration:
    def __init__(self, tipo):
        self.tipo = tipo

    def registrationType(self):
        if self.tipo == 'eleitor':
            fileEleitores = './data/eleitores.txt'
            pathKeys = '../../data/tre/keys_eleitores'
            self.registerKeys(fileEleitores, pathKeys)
    
    def registerKeys(self, file, keys): 
        file = File(file)
        gpg = gnupg.GPG(homedir=keys)
        gpg.encoding = 'utf-8'

        cont = 0
        texto = file.read()
        for linha in texto:
            print(linha)
            nome = linha.split(',')[0]
            print(nome)
            cont += 1
        
        print(cont)

            # input = gpg.gen_key_input( 
            #     name_real = nome,
            #     expire_date = '2025-04-01',
            #     key_type = 'RSA',
            #     key_length = 4096,
            #     key_usage = '',
            #     subkey_type = 'RSA',
            #     subkey_length = 4096,
            #     subkey_usage = 'encrypt,sign,auth',
            #     passphrase = 'sekrit'
            # )
            # gpg.gen_key(input)