from nltk.corpus import PlaintextCorpusReader
from nltk.probability import *
from nltk import word_tokenize
import nltk, re, pprint
import matplotlib
#matplotlib.use("PDF")
from sympy.functions.elementary.complexes import principal_branch
from nltk.corpus import indian

corpus_root = "Emon Jubayer"


fl = open(corpus_root+"\\A (1).doc","r",encoding="utf8");
text = fl.read();
print(text[100:]);
tokens = word_tokenize(text);
#print(tokens);
ntext = nltk.Text(tokens);
print(ntext[5:50]);
#ntext.collocations()
#fdist = FreqDist(text);
#print(ntext.concordance("তাদের"))
print("\n\n\n\n\n")
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import tnt

#print(indian.tagged_sents())
print(indian.fileids())
train_data = indian.tagged_sents('bangla.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data) #Training the tnt Part of speech tagger with hindi data
print(tnt_pos_tagger.tag(nltk.word_tokenize("ফুলটা, গাছটা ছোট বেলায় হঠাৎ হঠাৎ দেখেছি পতিত ঘেসো জমিতে")));


