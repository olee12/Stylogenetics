import os
from nltk.tokenize import word_tokenize
import nltk;
from nltk.probability import FreqDist;
import errno


def getDect(word_list):
    word_dect = dict();
    for word in word_list:

        ara = word.split(",");
        if len(ara) < 2:
            continue;
        key = ara[0];
        val = ara[1];
        word_dect[key]= val;

    return word_dect;

def Freq_Sorbonam_word(rootFolder):

    fw = open("Sorbonam.txt","r",encoding="utf8");
    sorbonam_set = fw.read().split("\n");
    sorbonam_set = [s.strip() for s in sorbonam_set];
    allList = dict();
    to_save_folder = rootFolder
    folder_list = os.listdir(rootFolder);
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        files = os.listdir(rootFolder+"/"+folder+"/");
        for file in files:
            if file.find("data")!=-1:
                fw = open(rootFolder+"/"+folder+"/"+file,"r",encoding="utf8");
                raw_text = fw.read();
                word_freq = raw_text.split("\n");
                word_freq = word_freq[1:]
                allList[folder] = getDect(word_freq);

    allgramFile = " ,";
    keys = sorted(allList.keys());
    for key in keys :
        allgramFile+=key;
        allgramFile+=",";

    allgramFile = allgramFile[:len(allgramFile)-1];
    allgramFile+="\n"

    for word in sorbonam_set:
        allgramFile += word;
        for key in keys:
            dic = dict(allList[key]);
            val = dic.get(word,"0");
            allgramFile+=","
            allgramFile+=val;

        allgramFile+="\n";
    fw = open(rootFolder+"/"+"Freq_Sorbonam"+".csv","w",encoding="utf8");
    fw.write(allgramFile);
    fw.close();



Freq_Sorbonam_word("#Sorbonam[.]")