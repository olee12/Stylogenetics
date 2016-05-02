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
alphabet_list = "[() ,“–!?_”.<>\"“‘‘ ’‘‘;*’%-=$#{}+-|‘~`/—-¯-—%—/﻿/﻿﻿':।]∆+";
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


def sentanceLenFrequency():
    to_save_folder = "./#SentanceLenFreq[.]/"
    folder_list = os.listdir("./");
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        data_path = folder_name + "data.doc";
        fw = open(data_path, "r", encoding="utf8");
        text = fw.read();
        words = word_tokenize(text);
        sents = getSentancesTokens(text);
        freq=[]
        for sent in sents:
            sent_len = getSentanceLen(sent);
            if sent_len==120:
                print(sent);
            if sent_len>0:
                freq.append(sent_len)

        fdist = FreqDist(freq);
        keys = fdist.most_common();
        dataFreq = "Sentance Len,Freqency\n"
        for key in sorted(keys):
            dataFreq+= str(key[0])+","+str(key[1]) +"\n";
        make_sure_path_exists(to_save_folder + folder)
        writer = open(to_save_folder + folder + "/" + folder + "[SentanceLen_Freq].csv", "w+", encoding="utf8");
        writer.write(dataFreq);
        fw.close();
        writer.close();



def wordLenFrequency():
    to_save_folder = "./#WordLenFreq[.]/"
    folder_list = os.listdir("./");
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        data_path = folder_name + "data.doc";
        fw = open(data_path, "r", encoding="utf8");
        text = fw.read();
        words = word_tokenize(text);

        freq=[]
        for word in words:
            word_len = getWordLen(word);
            if word_len==1:
                print(word);
            if word_len>0:
                freq.append(word_len)

        fdist = FreqDist(freq);
        keys = fdist.most_common();
        dataFreq = "Word Len,Freqency\n"
        for key in sorted(keys):
            dataFreq+= str(key[0])+","+str(key[1]) +"\n";
        make_sure_path_exists(to_save_folder + folder)
        writer = open(to_save_folder + folder + "/" + folder + "[WordLen_Freq].csv", "w+", encoding="utf8");
        writer.write(dataFreq);
        fw.close();
        writer.close();



sentanceLenFrequency();
wordLenFrequency();
#print(" দাড়িয়ে "+str(getWordLen("দাড়িয়ে")))
#print(alphabet_list.find("য়"));
#print(alphabet_list.find("ড়"));
#sentanceLenFrequency();
#wordLenFrequency()
