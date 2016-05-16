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
        key = ara[0].strip();
        val = ara[1];
        word_dect[key]= val;

    return word_dect;

def Freq_filtered_one_word(rootFolder):
    fw = open(rootFolder+"/Filterd Word Phase 1.txt","r",encoding="utf8");
    filtered = fw.read().split("\n");
    filtered = [word.strip() for word in filtered];
    print(filtered[:30])
    word_set = sorted(set(filtered));
    #sortedword = "";
    #for word in word_set:
        #sortedword+=word;
        #sortedword+="\n";
    #fw = open(rootFolder + "/Filterd Word Phase 1.txt", "w", encoding="utf8");
    #fw.write(sortedword);
    allList = dict();
    to_save_folder = rootFolder
    folder_list = os.listdir(rootFolder);
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        files = os.listdir(rootFolder+"/"+folder+"/");
        for file in files:
            if file.find("_Freq")!=-1:
                fw = open(rootFolder+"/"+folder+"/"+file,"r",encoding="utf8");
                raw_text = fw.read();
                word_freq = raw_text.split("\n");
                allList[folder] = getDect(word_freq);
                print(word_freq[:50])

    allgramFile = " ,";
    keys = sorted(allList.keys());
    for key in keys :
        allgramFile+=key;
        allgramFile+=",";

    allgramFile = allgramFile[:len(allgramFile)-1];
    allgramFile+="\n"

    for word in word_set:
        allgramFile += word;
        for key in keys:
            dic = dict(allList[key]);
            val = dic.get(word,"0");
            allgramFile+=","
            allgramFile+=val.strip();
            print(dic.get("না",0));

        allgramFile+="\n";
    fw = open(rootFolder+"/"+"Filtered_one_word"+".csv","w",encoding="utf8");
    fw.write(allgramFile);
    fw.close();




def Freq_common_word_change_one_word(rootFolder):
    fw = open(rootFolder+"/Common word change.txt","r",encoding="utf8");
    filtered = fw.read().split("\n");
    filtered = [word.strip() for word in filtered];
    print(filtered[:30])
    word_set = sorted(set(filtered));
    #sortedword = "";
    #for word in word_set:
        #sortedword+=word;
        #sortedword+="\n";
    #fw = open(rootFolder + "/Filterd Word Phase 1.txt", "w", encoding="utf8");
    #fw.write(sortedword);
    allList = dict();
    to_save_folder = rootFolder
    folder_list = os.listdir(rootFolder);
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        files = os.listdir(rootFolder+"/"+folder+"/");
        for file in files:
            if file.find("_Freq")!=-1:
                fw = open(rootFolder+"/"+folder+"/"+file,"r",encoding="utf8");
                raw_text = fw.read();
                word_freq = raw_text.split("\n");
                allList[folder] = getDect(word_freq);
                print(word_freq[:50])

    allgramFile = " ,";
    keys = sorted(allList.keys());
    for key in keys :
        allgramFile+=key;
        allgramFile+=",";

    allgramFile = allgramFile[:len(allgramFile)-1];
    allgramFile+="\n"

    for word in word_set:
        allgramFile += word;
        for key in keys:
            dic = dict(allList[key]);
            val = dic.get(word,"0");
            allgramFile+=","
            allgramFile+=val.strip();

        allgramFile+="\n";
    fw = open(rootFolder+"/"+"Common_word_changed_freq"+".csv","w",encoding="utf8");
    fw.write(allgramFile);
    fw.close();


Freq_common_word_change_one_word("#Unigram[.]")

Freq_filtered_one_word("#Unigram[.]")