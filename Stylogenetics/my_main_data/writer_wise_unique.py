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
        make_sure_path_exists("UniqueWords[.]/"+writer)
        print("UniqueWords[.]/"+writer)
        fw = open("./UniqueWords[.]/"+writer+"/"+writer+"[UniqueWords].csv","w",encoding="utf8");
        fw.write(uniqueWordByWriter);
        fw = open("./UniqueWords[.]/"+writer+"/"+writer+"[UniqueWords_Freq].csv","w",encoding="utf8");
        fw.write(uniqueWordByWriterFreq);



UniqueWords();


