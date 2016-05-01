import nltk
from nltk.corpus import indian
from nltk.util import bigrams

print(indian.words())
# print(indian.raw())
print(indian.fileids())

print(indian.words('bangla.pos'))
word = indian.raw('bangla.pos');
print(indian.tagged_words('bangla.pos'))
#for i in indian.sents('bangla.pos'):
#    print(i);

indian.readme()
# print(word);
# file = open("bangla_tag_POS.xml","w",encoding="utf8");
# file.write(word);
# file.close()
