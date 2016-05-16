import os
from nltk.tokenize import word_tokenize
import nltk;
from nltk.probability import FreqDist;
import errno
biram_file = open("biram.txt","r",encoding="utf8")
biram_text = biram_file.read();
biram = biram_text;
from nltk.util import bigrams;
stop_sent = "।!?"
cnt = 1;

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise




def UniqueWords():
    allList = dict();
    rootFolder = "./"
    to_save_folder = rootFolder
    folder_list = os.listdir(rootFolder);
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        fw = open(rootFolder+"/"+folder+"/"+"data.doc","r",encoding="utf8");
        words = word_tokenize(fw.read());
        allList[folder] = FreqDist(w for w in words if len(w)>1 and w!="``");
        print(allList[folder]["sdfasadfasdfas"]);

    writers = allList.keys();
    uniqueWordByWriter = "";
    uniqueWordByWriterFreq = "";
    for writer in writers:
        fdist = allList[writer];
        print(writer);
        uniqueWordByWriter = "";
        uniqueWordByWriterFreq = "";
        for key in fdist.most_common():
            #print(key)
            flag = 1;
            for other_writer in writers:
                if other_writer!=writer:
                    if allList[other_writer][key[0]] >5 :
                        #print(other_writer+" "+str(allList[other_writer][key[0]]));
                        flag = 0;
            if flag:
                uniqueWordByWriter += key[0];
                uniqueWordByWriter += "\n";
                uniqueWordByWriterFreq += key[0] + "," + str(key[1]) + "\n";
                #print(writer + " " + uniqueWordByWriter);
        make_sure_path_exists("#UniqueWords[.]/"+writer)
        print("#UniqueWords[.]/"+writer)
        fw = open("./#UniqueWords[.]/"+writer+"/"+writer+"[UniqueWords].csv","w",encoding="utf8");
        fw.write(uniqueWordByWriter);
        fw = open("./#UniqueWords[.]/"+writer+"/"+writer+"[UniqueWords_Freq].csv","w",encoding="utf8");
        fw.write(uniqueWordByWriterFreq);


def allUniqueWord(rootFolder):
    allList = dict();
    to_save_folder = rootFolder
    folder_list = os.listdir(rootFolder);
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        files = os.listdir(rootFolder + "/" + folder + "/");
        for file in files:
            if file.find("_Freq") != -1:
                fw = open(rootFolder + "/" + folder + "/" + file, "r", encoding="utf8");
                allList[folder] = fw.read();

    allgramFile = "";
    keys = sorted(allList.keys());
    for key in keys:
        allList[key] = str(allList[key]).split("\n");
        allgramFile += key;
        allgramFile += ","
        allgramFile += "value";
        allgramFile += ",";

    allgramFile = allgramFile[:len(allgramFile) - 1];
    allgramFile += "\n"
    for i in range(0, 80):
        f = 0
        for key in keys:
            print(key + ":::" + allList[key][i]);
            if f != 0:
                allgramFile += ",";
            f = 1;
            allgramFile += allList[key][i];
        print("\n")
        allgramFile += "\n";

    fw = open(rootFolder + "/" + "All" + rootFolder[2:] + ".csv", "w", encoding="utf8");
    fw.write(allgramFile);
    fw.close();






UniqueWords();
allUniqueWord("#UniqueWords[.]")


