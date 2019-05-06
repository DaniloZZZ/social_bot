import sys
import numpy as np
from w2v import main as w2v
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import OneHotEncoder

def load_from_file(fname):
    with open(fname,'r+') as f:
        result = f.read()
    return result

def load_unique_words(fname):
    words = set()
    with open(fname,'r+') as f:
        for i, line in enumerate(f):
            line_words = set( line.split() )
            words = words.union(line_words)
    return words

class MessageDataset(Dataset):
    def __init__(self, path):
        """
        Args:
            path: path to file of messages
        """
        self.path=path
        self.raw = load_from_file(path)
        self.data = self.raw.split()
        self.words = set(self.data)
        self._encoder = OneHotEncoder()
        d = np.array(self.data).reshape(-1,1)
        self._encoder.fit(d)
        self.data = np.array(self._encoder.transform(d).todense())
        print(self.data.shape)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        N = 3
        word = self.data[idx]
        #elem = lambda word: self._encoder.transform([[word]]).todense()
        answer =np.array(
            np.concatenate(
                (
                self.data[idx-N:idx],
                self.data[idx+1:idx+1+N]
                )
            )
        )
        return np.array((word)), np.sum(answer, axis = 0)

def main():
    filename = sys.argv[1]
    print("loading words")
    words = load_unique_words(filename)
    print(words)
    print(len(words))
    dataset =MessagesDataset(filename)
    N=  100
    print(f"dataset idx {N}")
    elem =dataset[N] 
    print(elem)
    print(sum(elem[0]))
    print(sum(elem[1]))

if __name__=="__main__":

    main()
