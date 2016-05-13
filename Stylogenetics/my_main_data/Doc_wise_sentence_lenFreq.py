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


def sentanceLenFrequency():
    to_save_folder = "./#DocWiseSentanceLenFreq[.]/"
    folder_list = os.listdir("./");

    for folder in folder_list:
        allList = dict();
        lenDic = dict()
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        file_list = os.listdir(folder_name);
        file_list = sorted(file_list);
        allSenFreqText = ",";
        for file in file_list:
            if file.find("Normal")==-1:
                continue;
            allSenFreqText+=file;
            allSenFreqText+=",";

        allSenFreqText = allSenFreqText[:len(allSenFreqText)-1] + "\n"

        for file in file_list:
            if file.find("Normal")==-1:
                continue;
            data_path = folder_name+"/"+file;
            fw = open(data_path, "r", encoding="utf8");
            text = fw.read();
            sents = getSentancesTokens(text);
            totSen = 0.0;
            freq=[]
            for sent in sents:
                sent_len = getSentanceLen(sent);

                if sent_len>0:
                    totSen+=1;
                    freq.append(sent_len)
            allList[file] = get_dict(freq);
            if totSen==0:
                print(file);
            lenDic[file] = totSen;

        keys = sorted(allList.keys());
        for i in range(1,30):
            allSenFreqText += str(i);

            for key in keys:
                allSenFreqText += ",";
                allSenFreqText += str(((allList[key][i])/lenDic[key]) * 100);
            allSenFreqText+="\n";
        make_sure_path_exists(to_save_folder + folder)
        writer = open(to_save_folder + folder + "/" + folder + "[ALLSentanceLen_Freq].csv", "w+", encoding="utf8");
        writer.write(allSenFreqText);
        fw.close();
        writer.close();



def get_dict(freq):
    mydic = dict();
    for i in range(1,30):
        mydic[i] = freq.count(i);

    return mydic;


sentanceLenFrequency();
#allSentanceLenFreq("#SentanceLenFreq[.]");
#wordLenFrequency();
#allSentanceLenFreq("#WordLenFreq[.]");
#sentanceLenFrequency();

#print(" দাড়িয়ে "+str(getWordLen("দাড়িয়ে")))
#print(alphabet_list.find("য়"));
#print(alphabet_list.find("ড়"));
#sentanceLenFrequency();
#wordLenFrequency()
