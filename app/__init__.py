from voting import Voting
from keyGeneration import KeyGeneration
from loadFiles import LoadFiles

if __name__ == '__main__':
    print('teste')
    LoadFiles('./data')

    Voting().startVoting()
