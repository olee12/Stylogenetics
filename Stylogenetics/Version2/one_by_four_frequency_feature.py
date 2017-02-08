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




def one_by_four(path,top=50):
    root_path = "./"+path;
    writers = os.listdir(root_path);
    word_set = set();
    temp_set = set();
    writer_table = dict();
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

        words = getWordList(formated_text);
        fdist = FreqDist(w for w in words if
                         len(w) > 1 and isEnglish(w) == False and w != "``");
        keys = fdist.most_common(top);
        print(keys);
        writer_table[writer] = dict(keys);
        for key in keys:
            temp_set.add(key[0]);

    writers = writer_table.keys();
    for word in temp_set:
        for writer1 in writers:
            freq1 = writer_table[writer1].get(word,0);
            for writer2 in writers:
                if writer2 == writer1:
                    continue;
                freq2 = writer_table[writer2].get(word,0);
                if freq1  >= freq2*4:
                    print(writer1+" "+writer2+" "+str(freq1)+" " + str(freq2)+ " "+word);
                    word_set.add(word);





    print(word_set);
    fw = open("./Features/Modified word frequency.csv","w",encoding="utf8");
    for word in word_set:
        fw.write(word);
        fw.write("\n");
    fw.close();




one_by_four("Train Data",300);