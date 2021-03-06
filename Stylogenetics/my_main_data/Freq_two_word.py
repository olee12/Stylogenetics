import os
from nltk.tokenize import word_tokenize
import nltk;
from nltk.probability import FreqDist;
import errno

def isEnglish(word):
    for char in word:
        if char>='a' and char<='z':
            return False;
        elif char >= "A" and char <= "Z":
            return False;
    return True;

def getDect(word_list):
    word_dect = dict();
    for word in word_list:

        ara = word.split(",");
        if len(ara) < 2:
            continue;
        key = ara[0];
        val = ara[1];
        #print(key+" "+val);
        word_dect[key]= val;

    return word_dect;

def Freq_two_word(rootFolder):
    word_set = set()
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
                word_freq = word_freq[:len(word_freq)-1];
                word_freq = [word for word in word_freq if isEnglish(word)==True]
                print(word_freq[:50])
                print("********* "+folder+ " *********");
                word_freq = word_freq[:80]
                allList[folder] = getDect(word_freq);

                for i in range(0,70):
                    if i >= len(word_freq):
                        break;
                    print(word_freq[i]);
                    word_set.add(word_freq[i].split(",")[0]);


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
            allgramFile+=val;

        allgramFile+="\n";
    fw = open(rootFolder+"/"+"Freq_two_word"+".csv","w",encoding="utf8");
    fw.write(allgramFile);
    fw.close();



Freq_two_word("#Bigram[.]")