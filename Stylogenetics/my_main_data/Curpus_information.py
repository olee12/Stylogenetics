import os
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk;
from nltk.probability import FreqDist;
import errno
biram_file = open("biram.txt","r",encoding="utf8")
biram_text = biram_file.read();
biram = biram_text;
from nltk.util import bigrams;
stop_sent = "।!?"
cnt = 1;
alphabet_list = "[() ,“–!?_”.<>\"“‘‘ ’‘‘;*’%-=$#{}+-|‘~`/—-¯-—%—/﻿/﻿﻿':।]∆+্";
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            pass

def formatText(text):
    mytext = "";
    for char in text:
        if biram_text.find(char) != -1:
            mytext += " ";
        mytext = mytext + char
        if biram_text.find(char) != -1:
            mytext += " ";
    return mytext;

def getWordList(text):
    tokens = word_tokenize(text);
    return tokens


def getSentancesTokens(text):
    text = text.replace(" ।", " . ")
    text = text.replace("|", " . ")
    sents = sent_tokenize(text);
    sents = [sent for sent in sents]
    return sents;


def getWordLen(word):
    cnt = 0;
    for char in word:
        if alphabet_list.find(char)!=-1:
            continue;
        cnt+=1;

    return cnt;

def getSentanceLen(sent):
    sen_len = 0;
    words = word_tokenize(sent)
    for word in words:
        if getWordLen(word)>=1:
            sen_len+=1;
    return sen_len;


def type_token_ratio():
    to_save_folder = "./#TypeTokenRatio[.]/"
    folder_list = os.listdir("./");
    totalWord = 0;
    docWiseData = "";
    defaultData = "";
    modifiedData = "";

    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        data_path = folder_name + "data.doc";
        fw = open(data_path, "r", encoding="utf8");
        text = fw.read();
        wordList = getWordList(text);
        wordList = [w for w in wordList if len(w)>1];
        totalWord += len(wordList);
        print(folder + " "+str(len(wordList)));

    print("Total Word = "+str(totalWord));








def get_dict(freq):
    mydic = dict();
    for i in range(1,30):
        mydic[i] = freq.count(i);

    return mydic;



type_token_ratio();
#allSentanceLenFreq("#SentanceLenFreq[.]");
#wordLenFrequency();
#allSentanceLenFreq("#WordLenFreq[.]");
#sentanceLenFrequency();

#print(" দাড়িয়ে "+str(getWordLen("দাড়িয়ে")))
#print(alphabet_list.find("য়"));
#print(alphabet_list.find("ড়"));
#sentanceLenFrequency();
#wordLenFrequency()
