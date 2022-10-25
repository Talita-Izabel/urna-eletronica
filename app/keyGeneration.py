import os
import pwd
import gnupg
from file import File

path = os.getcwd() + "/app/config/env.json"
env = File(path).readJSON()

gpg = gnupg.GPG(gnupghome=env['gnupghome'])
gpg.encoding = 'utf-8'

def gerarChaveTSE():
    tse_input = gpg.gen_key_input( 
        name_real = 'tse',
        key_type = 'RSA',
        key_length = 1024,
        passphrase = env['password']
    )

    tse_key = gpg.gen_key(tse_input)

    pubkey = gpg.export_keys(tse_key.fingerprint)
    seckey = gpg.export_keys(tse_key.fingerprint, True, passphrase='0912UE')

    print(gpg.import_keys(pubkey))

    gpg.trust_keys(tse_key.fingerprint, 'TRUST_ULTIMATE')

def gerarChaveCartorioUrna():
    fingerprintTSE = '820495A1FC892FD2D4AB2E7EC5177B1B1397B038'

    cartorio_input = gpg.gen_key_input( 
        name_real = 'cartorio',
        key_type = 'RSA',
        key_length = 1024,
        passphrase = env['password']
    )

    cartorio_key = gpg.gen_key(cartorio_input)

    pubkey = gpg.export_keys(cartorio_key.fingerprint)
    seckey = gpg.export_keys(cartorio_key.fingerprint, True, passphrase='0912UE')

    print(gpg.import_keys(pubkey))

    # Assina
    os.system(f'gpg -u {fingerprintTSE} --sign-key {cartorio_key.fingerprint}')

    print(gpg.trust_keys(cartorio_key.fingerprint, 'TRUST_ULTIMATE'))

    # ------------------------------------------------------------------------------
    urna_input = gpg.gen_key_input( 
        name_real = 'urna',
        key_type = 'RSA',
        key_length = 1024,
        passphrase = env['password']
    )

    urna_key = gpg.gen_key(urna_input)

    pubkey = gpg.export_keys(urna_key.fingerprint)
    seckey = gpg.export_keys(urna_key.fingerprint, True, passphrase='0912UE')

    print(gpg.import_keys(pubkey))

    # Assina
    os.system(f'gpg -u {fingerprintTSE} --sign-key {urna_key.fingerprint}')

    print(gpg.trust_keys(urna_key.fingerprint, 'TRUST_ULTIMATE'))

def gerarMesario():
    fingerprintCartorio = '8A80A5E631D800E3B3E66B08E6E151AE8D863322'

    mesario_input = gpg.gen_key_input( 
        name_real = 'mesario',
        key_type = 'RSA',
        key_length = 1024,
        passphrase = env['password']
    )

    masario_key = gpg.gen_key(mesario_input)

    pubkey = gpg.export_keys(masario_key.fingerprint)
    seckey = gpg.export_keys(masario_key.fingerprint, True, passphrase='0912UE')

    print(gpg.import_keys(pubkey))

    # Assina
    os.system(f'gpg -u {fingerprintCartorio} --sign-key {masario_key.fingerprint}')

    print(gpg.trust_keys(masario_key.fingerprint, 'TRUST_ULTIMATE'))

def gerarChavesEleitores():
    fingerprintCartorio = '8A80A5E631D800E3B3E66B08E6E151AE8D863322'

    path = os.getcwd() + '/data/eleitores.txt'

    texto = File(path).read()

    for eleitor in texto:
        nome = eleitor.split(',')[0]
        eleitor_input = gpg.gen_key_input( 
            name_real = nome,
            key_type = 'RSA',
            key_length = 1024,
            passphrase = env['password']
        )

        eleitor_key = gpg.gen_key(eleitor_input)

        pubkey = gpg.export_keys(eleitor_key.fingerprint)
        seckey = gpg.export_keys(eleitor_key.fingerprint, True, passphrase='0912UE')

        print(gpg.import_keys(pubkey))

        # Assina
        os.system(f'gpg -u {fingerprintCartorio} --sign-key {eleitor_key.fingerprint}')

        print(gpg.trust_keys(eleitor_key.fingerprint, 'TRUST_ULTIMATE'))

def listaChaves():
    print(gpg.list_keys(True))

listaChaves()
