import nltk
import re
import time

word_to_be_tagged = "ताजो स्वास आनी चकचकीत दांत तुमचें व्यक्तीमत्व परजळायतात."

word_to_be_tagged_next = "दांत आशिल्ल्यान तुमचो आत्मविश्वासय वाडटा."

from nltk.corpus import indian

train_data = indian.tagged_sents('hindi.pos')[:300]
test_data = indian.tagged_sents('hindi.pos')[301:]

print(word_to_be_tagged)
print(train_data)
from nltk.tag import tnt

train_data = indian.tagged_sents('hindi.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data) #Training the tnt Part of speech tagger with hindi data
print("hello world");
print(tnt_pos_tagger.tag(nltk.word_tokenize(word_to_be_tagged)))