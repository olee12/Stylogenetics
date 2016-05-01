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


def unigramAGivenFolder(folder):
    to_save_folder = "./#Unigram[.]/"
    folder_name = "./" + folder + "/"
    data_path = folder_name + "data.doc";
    fw = open(data_path, "r", encoding="utf8");
    text = fw.read();
    print(len(text))
    #text = text[:10000];
    words = word_tokenize(text);
    fdist = FreqDist(w for w in words if len(w) > 1 and w != "``");

    keys = fdist.most_common(len(fdist.keys()))
    dataFreq = "";
    for key in keys:
        dataFreq += str(key[0]) + " , " + str(key[1]) + "\n";

    make_sure_path_exists(to_save_folder + folder)
    writer = open(to_save_folder + folder + "/" + folder + "[unigram].csv", "w+", encoding="utf8");
    writer.write(dataFreq);
    fw.close();
    writer.close();


def BigramAGivenFolder(folder):
    to_save_folder = "./#Bigram[.]/"
    folder_name = "./" + folder + "/"
    data_path = folder_name + "data.doc";
    fw = open(data_path, "r", encoding="utf8");
    text = fw.read();
    words = word_tokenize(text);

    big = list(bigrams(w for w in words if len(w) > 1 and w != "``"));
    myBig = []
    for bi in big:
        myBig.append(bi[0] + " " + bi[1]);

    fdist = FreqDist(str(w) for w in myBig);

    keys = fdist.most_common(len(fdist.keys()))
    dataFreq = "";
    for key in keys:
        dataFreq += str(key[0]) + " , " + str(key[1]) + "\n";

    make_sure_path_exists(to_save_folder + folder)
    writer = open(to_save_folder + folder + "/" + folder + "[bigram].csv", "w+", encoding="utf8");
    writer.write(dataFreq);
    fw.close();
    writer.close();

def trigramAGivenFolder(folder):
    to_save_folder = "./#Trigram[.]/"
    folder_name = "./" + folder + "/"
    data_path = folder_name + "data.doc";
    fw = open(data_path, "r", encoding="utf8");
    text = fw.read();
    words = word_tokenize(text);
    valid_word = [w for w in words if len(w) > 1 and w != "``"];
    tri_list = [];
    vlen = len(valid_word);
    for i in range(0, vlen - 2):
        tri_list.append(valid_word[i] + " " + valid_word[i + 1] + " " + valid_word[i + 2]);

    fdist = FreqDist(w for w in tri_list);

    keys = fdist.most_common(len(fdist.keys()))
    dataFreq = "";
    for key in keys:
        dataFreq += str(key[0]) + "," + str(key[1]) + "\n";

    make_sure_path_exists(to_save_folder + folder)
    writer = open(to_save_folder + folder + "/" + folder + "[Triram].csv", "w+", encoding="utf8");
    writer.write(dataFreq);
    fw.close();
    writer.close();




unigramAGivenFolder("Tareque Anu")
BigramAGivenFolder("Tareque Anu")
trigramAGivenFolder("Tareque Anu")