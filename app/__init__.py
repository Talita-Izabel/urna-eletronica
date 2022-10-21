from voting import Voting
from loadFiles import LoadFiles
# from keyGeneration import KeyGeneration

if __name__ == '__main__':
    LoadFiles('./data')
    Voting().startVoting()
