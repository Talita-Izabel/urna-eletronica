import os
import gnupg
from file import File
from unicodedata import normalize

 # for eleitor in text:
    #     # Pega o nome remove acentos e coloca - no lugar de espaço
    #     name = eleitor.split(',')[0]
    #     nameFile = name.replace(' ', '-').lower()
    #     nameFile = normalize('NFKD', nameFile).encode('ASCII','ignore').decode('ASCII')

def exportPublicKeys():
    path = os.getcwd() + "/app/config/env.json"
    env = File(path).readJSON()

    gpg = gnupg.GPG(gnupghome=env['gnupghome'])
    gpg.encoding = 'utf-8'
    pathPub = '/home/talita/Documentos/TSI/6_Periodo/seguranca/trabalho/keys/pub'
    pathPriv = '/home/talita/Documentos/TSI/6_Periodo/seguranca/trabalho/keys/priv'

    pub_keys = gpg.list_keys()
    for i in pub_keys:
        fingerprint = i['fingerprint']
        name = i['uids'][0].split('<')[0].strip()
        nameFile = name.replace(' ', '-').lower()
        nameFile = normalize('NFKD', nameFile).encode('ASCII','ignore').decode('ASCII')

        print(name, nameFile, fingerprint)

        # Gerando chaves publicas0912UE0912UE
        os.system(f'gpg --export -a {fingerprint} > {pathPub}/pub-{nameFile}.pem')

        # Gerando chaves privadas
        #os.system(f'gpg --export-secret-keys -a {fingerprint} > {pathPriv}/priv-{nameFile}.pem')

def exportPrivKeys():
    path = os.getcwd() + "/app/config/env.json"
    env = File(path).readJSON()

    gpg = gnupg.GPG(gnupghome=env['gnupghome'])
    gpg.encoding = 'utf-8'
    pathPub = '/home/talita/Documentos/TSI/6_Periodo/seguranca/trabalho/keys/pub'
    pathPriv = '/home/talita/Documentos/TSI/6_Periodo/seguranca/trabalho/keys/priv'

    pub_keys = gpg.list_keys()
    for i in pub_keys:
        fingerprint = i['fingerprint']
        name = i['uids'][0].split('<')[0].strip()
        nameFile = name.replace(' ', '-').lower()
        nameFile = normalize('NFKD', nameFile).encode('ASCII','ignore').decode('ASCII')

        print(name, nameFile, fingerprint)

        # Gerando chaves privadas
        os.system(f'gpg --export-secret-keys -a {fingerprint} > {pathPriv}/priv-{nameFile}.pem')

exportPrivKeys() 
