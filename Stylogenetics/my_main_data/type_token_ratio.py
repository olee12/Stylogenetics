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
    totTatalWord = 0;
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
        words = word_tokenize(text);
        words = [word for word in words if len(word)>1]


        totTatalWord = len(words);
        tot = 0;
        prv = 0;
        freq = []
        for i in range(1000,totTatalWord,1000):
            nword = words[prv:i];
            prv = i;
            freq.append((len(set(nword))/len(nword)) * 100)
            tot+= ((len(set(nword))/len(nword)) * 100)

        mtypeToken = (tot/len(freq))
        typeToken = (len(set(words))/len(words)) * 100;
        print(folder_name+" Original " +str(typeToken));
        print(folder_name+" Modified " +str(mtypeToken));

        files = os.listdir("./"+folder_name+"/");

        tot = 0;
        freq = [];
        avg_word = 0;
        for file in files:
            if file.find("Normal")==-1:
                continue;
            data_path = "./"+folder_name+"/"+file;
            fw = open(data_path,"r",encoding="utf8");
            text = fw.read();
            words = getWordList(text);
            words = [word for word in words if len(word)>1];
            if len(words)==0:
                continue;
            tot += ((len(set(words)) / len(words))*100)
            freq.append(((len(set(words)) / len(words))*100))
            avg_word+=len(words);
        doctypeToken = tot / len(freq);
        print(folder_name + " DocWise " + str(doctypeToken));
        print(folder_name + " avg word " + str(avg_word/len(freq)));
        print(folder_name + " tot _ doc " + str(len(freq)));
        print(" ");
        modifiedData+= folder+","+str(mtypeToken)+"\n";
        defaultData+= folder+","+str(typeToken)+"\n";
        docWiseData+= folder +","+str(doctypeToken)+"\n";


    make_sure_path_exists(to_save_folder);
    fw = open(to_save_folder + "/"+ "[Original]" + ".csv", "w", encoding="utf8");
    fw.write(defaultData)
    fw = open(to_save_folder + "/"+ "[Modified]" + ".csv", "w", encoding="utf8");
    fw.write(modifiedData)
    fw = open(to_save_folder + "/"+ "[DocWise]" + ".csv", "w", encoding="utf8");
    fw.write(docWiseData);
    fw.close();






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
