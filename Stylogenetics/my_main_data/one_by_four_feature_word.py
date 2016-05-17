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
        key = ara[0].strip();
        val = ara[1];
        word_dect[key]= val;

    return word_dect;

def one_by_four_feature_word(rootFolder):
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
                word_freq = word_freq[:450];
                allList[folder] = getDect(word_freq);

                for i in range(0,150):
                    word_set.add(word_freq[i].split(",")[0]);

    word_set = sorted(word_set);

    one_by_four_word_list = set();

    keys = sorted(allList.keys());
    for word in word_set:
        for key1 in keys:
            flag = 0;
            freq1 = int(allList[key1].get(word,0));
            freq1 /= 4;
            for key2 in keys:
                if key1==key2:
                    continue;
                freq2 = int(allList[key2].get(word,0));
                if freq2 <= freq1:
                    one_by_four_word_list.add(word);
                    flag = 1;

            if flag==1:
                break;

    data_path = rootFolder+"/"+"one_by_four_feature_words.csv";
    allgram = "";
    for word in sorted(one_by_four_word_list):
        if isEnglish(word)==False:
            continue;
        allgram+=word;
        allgram+="\n";
    fw = open(data_path,"w",encoding="utf8");
    fw.write(allgram);



def Freq_one_by_four_feature_word(rootFolder):
    fw = open(rootFolder+"/one_by_four_feature_words.csv","r",encoding="utf8");
    filtered = fw.read().split("\n");
    filtered = filtered[:len(filtered)-1];
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
    fw = open(rootFolder+"/"+"Freq_one_by_four_feature_words"+".csv","w",encoding="utf8");
    fw.write(allgramFile);
    fw.close();



Freq_one_by_four_feature_word("#Unigram[.]")
one_by_four_feature_word("#Unigram[.]")