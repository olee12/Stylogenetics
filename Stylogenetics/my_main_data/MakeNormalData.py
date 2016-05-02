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
    print(tokens[:100]);
    return tokens

def isWordEnglish(word):
    str = "qwertyuiopppasdfghjkl;zxcvbnm,.963852741`=-qwertyuiopasdfghjklzxcvbnm,.QWERTUIOPASDFGHJKLZXCVBNM,"



def makeRootFolderNormal():
    folder_list = os.listdir("./");
    for folder in folder_list:
        if folder.find(".") != -1:
            continue;
        folder_name = "./" + folder + "/"
        file_list = os.listdir(folder_name)
        mainText = ""
        for file in file_list:
            if (file.find("Normal") != -1) or (file == "data.doc"):
                continue;
            tmp_text ="";
            fw = open(folder_name + file, "r", encoding="utf-8")
            print(file)
            text = fw.read();
            print(len(text));
            formated_text = formatText(text);
            mainText += formated_text
            mainText += "\n\n\n\n\n";
            tmp_text+= formated_text;
            fw.close();
            ## creating new fromated file
            fw = open(folder_name + "Normal_"+file, "w", encoding="utf-8")
            fw.write(tmp_text);
            fw.close();

        fw = open(folder_name + "data.doc", "w", encoding="utf8");
        fw.write(mainText)



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
        writer = open(to_save_folder+folder+"/"+folder+"[unigram_Freq].csv","w+",encoding="utf8");
        writer.write(dataFreq);
        fw.close();
        writer.close();


def unigramForGiverTokens(words):
    fdist = FreqDist(w for w in words if len(w) > 1);
    keys = fdist.most_common(len(fdist.keys()))
    return keys



def testFunc():
    fw = open("./MZI/data.doc", "r", encoding="utf8");
    text = fw.read();
    tockens = getWordList(text)
    print(len(set(tockens)))
    from nltk.probability import FreqDist
    from nltk.util import bigrams
    fdist = FreqDist(w for w in tockens if len(w) > 1);
    fdist.tabulate(50);
    big = list(bigrams(w for w in tockens if len(w) > 1));
    print(big[:100]);
    fdist = FreqDist(str(w) for w in big);
    fdist.tabulate(10);
    fdist.plot(50)


def makeGramForAll(rootFolder):
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
                allList[file] = fw.read();

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
        writer = open(to_save_folder+folder+"/"+folder+"[bigram_Freq].csv","w+",encoding="utf8");
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
        writer = open(to_save_folder + folder + "/" + folder + "[Triram_Freq].csv", "w+", encoding="utf8");
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
        writer = open(to_save_folder + folder + "/" + folder + "[Ngram_4_Freq].csv", "w+", encoding="utf8")
        writer.write(dataFreq)
        fw.close()
        writer.close()




#makeRootFolderNormal()
#unigramAll();
#BigramAll();
trigramAll();
#ngram4All();
makeGramForAll("./#Unigram[.]")
makeGramForAll("./#Bigram[.]")
makeGramForAll("./#Trigram[.]")
makeGramForAll("./#Ngram_4[.]")





