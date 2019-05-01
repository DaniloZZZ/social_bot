
import string
import sys

word_dict = {}
WINDOW = 3

def main():
    msg = sys.stdin.read()
    # remove all punctuation
    msg = msg.translate(str.maketrans('', '', string.punctuation))
    msg = msg.lower()
    print("message len",len(msg))
    words = msg.split()
    print("word count", len(words))

    for idx,word in enumerate(words):
        word_dict.setdefault(word,[])
        word_dict[word]+=words[idx-WINDOW:idx]+words[idx+1:idx+1+WINDOW]


    pairs = []
    for key, val in word_dict.items():
        word_dict[key] = set(word_dict[key])
        pairs.append((key, word_dict[key]))
    pairs.sort(key=lambda x:len(x[1]))
    for p in pairs:
        print(p)

if __name__=='__main__':
    main()
