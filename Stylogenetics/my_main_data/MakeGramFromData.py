import os
from nltk.tokenize import word_tokenize
import nltk;
from nltk.probability import FreqDist;

from nltk.util import bigrams;
stop_sent = "।!?"
cnt = 1;
import errno





def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            pass



def BigramAll():
    to_save_folder = "./#Bigram[.]/"
    folder_list = os.listdir("./");
    for folder in folder_list:
        if folder.find(".") != -1 :
            continue;
        folder_name = "./" + folder + "/"
        data_path = folder_name+"data.doc";
        fw = open(data_path,"r",encoding="utf8");
        text = fw.read();
        words = word_tokenize(text);

        big = list(bigrams(w for w in words if len(w) > 1 and w != "``"));
        myBig = []
        for bi in big:
            myBig.append(bi[0]+" "+bi[1]);

        fdist = FreqDist(str(w) for w in myBig);

        keys = fdist.most_common(len(fdist.keys()))
        dataFreq = "";
        for key in keys:
            dataFreq+= str(key[0])+" , "+str(key[1])+"\n";

        make_sure_path_exists(to_save_folder+folder)
        writer = open(to_save_folder+folder+"/"+folder+"[bigram].csv","w+",encoding="utf8");
        writer.write(dataFreq);
        fw.close();
        writer.close();



def trigramAll():
    to_save_folder = "./#Trigram[.]/"
    folder_list = os.listdir("./");
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        data_path = folder_name + "data.doc";
        fw = open(data_path, "r", encoding="utf8");
        text = fw.read();
        words = word_tokenize(text);
        valid_word = [w for w in words if len(w) > 1 and w != "``"];
        tri_list = [];
        vlen = len(valid_word);
        for i in range(0,vlen-2):
            tri_list.append(valid_word[i]+" "+valid_word[i+1]+" "+valid_word[i+2]);

        fdist = FreqDist(w for w in tri_list);

        keys = fdist.most_common(len(fdist.keys()))
        dataFreq = "";
        for key in keys:
            dataFreq += str(key[0])+ "," + str(key[1]) + "\n";

        make_sure_path_exists(to_save_folder + folder)
        writer = open(to_save_folder + folder + "/" + folder + "[Triram].csv", "w+", encoding="utf8");
        writer.write(dataFreq);
        fw.close();
        writer.close();



def ngram4All():
    to_save_folder = "./#Ngram_4[.]/"
    folder_list = os.listdir("./");
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        data_path = folder_name + "data.doc";
        fw = open(data_path, "r", encoding="utf8")
        text = fw.read();
        words = word_tokenize(text);
        valid_word = [w for w in words if len(w) > 1 and w != "``"]
        nlist4 = []
        vlen = len(valid_word);
        for i in range(0,vlen-3):
            nlist4.append(valid_word[i]+" "+valid_word[i+1]+" "+valid_word[i+2] + " " +valid_word[i+3])

        fdist = FreqDist(w for w in nlist4)
        keys = fdist.most_common(len(fdist.keys()))
        dataFreq = ""
        for key in keys:
            dataFreq += str(key[0])+ "," + str(key[1]) + "\n"
        make_sure_path_exists(to_save_folder + folder)
        writer = open(to_save_folder + folder + "/" + folder + "[Ngram_4].csv", "w+", encoding="utf8")
        writer.write(dataFreq)
        fw.close()
        writer.close()



def makeGramForAll(rootFolder):
    allList = dict();
    to_save_folder = rootFolder
    folder_list = os.listdir(rootFolder);
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        file = os.listdir(rootFolder+"/"+folder+"/");
        fw = open(rootFolder+"/"+folder+"/"+file[0],"r",encoding="utf8");
        allList[file[0]] = fw.read();

    allgramFile = "";
    keys = allList.keys();
    for key in keys :
        allList[key] = str(allList[key]).split("\n");
        key = key[:key.find("[")];
        allgramFile+=key;
        allgramFile+=","
        allgramFile+="value";
        allgramFile+=",";

    allgramFile = allgramFile[:len(allgramFile)-1];
    allgramFile+="\n"
    for i in range(0,50):
        f = 0
        for key in keys:
            print(key +":::"+allList[key][i]);
            if f!=0:
                allgramFile+=",";
            f = 1;
            allgramFile+=allList[key][i];
        print("\n")
        allgramFile+="\n";

    fw = open(rootFolder+"/"+"All"+rootFolder[2:]+".csv","w",encoding="utf8");
    fw.write(allgramFile);
    fw.close();


def unigramForGiverTokens(words):
    fdist = FreqDist(w for w in words if len(w) > 1);
    keys = fdist.most_common(len(fdist.keys()))
    return keys



def unigramAll():
    to_save_folder = "./#Unigram[.]/"
    folder_list = os.listdir("./");
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        data_path = folder_name+"data.doc";
        fw = open(data_path,"r",encoding="utf8");
        text = fw.read();
        words = word_tokenize(text);
        fdist = FreqDist(w for w in words if len(w) > 1 and w != "``");

        keys = fdist.most_common(len(fdist.keys()))
        dataFreq = "";
        for key in keys:
            dataFreq+= str(key[0])+" , "+str(key[1])+"\n";

        make_sure_path_exists(to_save_folder+folder)
        writer = open(to_save_folder+folder+"/"+folder+"[unigram].csv","w+",encoding="utf8");
        writer.write(dataFreq);
        fw.close();
        writer.close();