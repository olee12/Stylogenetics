import nltk;
from builtins import print
from nltk.corpus import indian;
from docutils.nodes import raw
from nltk import *
nltk.corpus.indian.fileids();
rawText = "";
for i in range(1,55):
    fileName = "Top\MZI\MZI"+str(i)+".doc";
    fw = open(fileName,"r",encoding="utf8");
    rawText+=fw.read();
    rawText+="\n";
    fw.close();

rawSen = rawText.split(" ");
rawSen1 = [sen.split("।") for sen in rawSen]
print(len(rawSen1));
mzi = Text(rawSen);
print(len(mzi));
fdist = FreqDist(mzi);
fdist.plot(50);

print(fdist["হবে"])



