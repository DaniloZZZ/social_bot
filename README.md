# Download all messages from social network and make a bot out of it.

- [x] Download from telegram
- [ ] Download from vk
- [ ] Convert to train ready database



## Plan

The most natural way to approach this problem is to use some flavour of RNN models.
There are two kinds of tags right now:

- <MSG>
- <PEER>

Which determine end of message and end of peer message sequence.

The task is to predict answer to previous message sequence.

## Questions

 - Should I use/train a word2vec model or train exactly from characters/words?

 - How a multi-layer RNN will perform? Use one RNN to character-wise encode words, than use another RNN to encode messages on top of it.

