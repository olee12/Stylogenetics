from sklearn import svm;
import os
from nltk.tokenize import word_tokenize
import nltk;
from nltk.probability import FreqDist;
import errno
import math;
biram_file = open("./train data/biram.txt","r",encoding="utf8")
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

def isEnglish(word):
    for char in word:
        if char>='a' and char<='z':
            return True;
        elif char >= "A" and char <= "Z":
            return True;
    return False;


def getWordList(text):
    tokens = word_tokenize(text);
    #print(tokens[:100]);
    return tokens

def isWordEnglish(word):
    str = "qwertyuiopppasdfghjkl;zxcvbnm,.963852741`=-qwertyuiopasdfghjklzxcvbnm,.QWERTUIOPASDFGHJKLZXCVBNM,"



def getDect(freq):
    word_dect = dict();
    for word in freq:
        key = word[0].strip();
        val = word[1];
        word_dect[key] = val;

    return word_dect;


def get_bigrams(raw_text):

    formated_text = formatText(raw_text);
    words = getWordList(formated_text);
    words = [word for word in words if len(word)>1 and word != "``" and word != "``"];
    words = [word for word in words if isEnglish(word)==False];
    myBigram = [];
    for i in range(0,len(words)-1):
        myBigram.append(words[i]+" "+words[i+1])
    return myBigram;

def most_frequent_words(path,top):
    root_path = "./"+path;
    writers = os.listdir(root_path);
    word_set = set();
    for writer in writers:
        if writer.find(".") != -1:
            continue;
        inside_folder = root_path + "//" +writer;
        files = os.listdir(inside_folder);
        formated_text = "";
        for file in files:
            file_path = root_path + "//" +writer+"//"+ file;
            fw = open(file_path,"r",encoding="utf8");
            article = fw.read();
            #print(article);
            formated_text+=" ";
            formated_text += formatText(article);
            fw.close();

        words = get_bigrams(formated_text);
        fdist = FreqDist(w for w in words if
                         len(w) > 1 and isEnglish(w) == False and w != "``");
        keys = fdist.most_common(top);
        for key in keys:
            #print(str(key[0]) + " , " + str(key[1]) + "\n");
            word_set.add(key[0]);
    print(word_set);
    fw = open("./Features/Bigrams.csv","w",encoding="utf8");
    for word in word_set:
        fw.write(word);
        fw.write("\n");
    fw.close();




most_frequent_words("Train Data",70);