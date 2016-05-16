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



def getWordList(text):
    tokens = word_tokenize(text);
    print(tokens[:100]);
    return tokens

def isWordEnglish(word):
    str = "qwertyuiopppasdfghjkl;zxcvbnm,.963852741`=-qwertyuiopasdfghjklzxcvbnm,.QWERTUIOPASDFGHJKLZXCVBNM,"

def getDect(freq):
    word_dect = dict();
    for word in freq:

        key = word[0].strip();
        val = word[1];
        word_dect[key]= val;

    return word_dect;

def makeWritersVectors(flag):
    if flag==1:
        fw = open("./train data/train_data.csv","r",encoding="utf8");
    else:
        fw = open("./train data/Filtered_one_word.csv","r",encoding="utf8");
    lines = fw.read().split("\n");

    head = lines[0];
    lines = lines[1:]
    writers=str(head[head.find(",")+1:]).split(",");
    print(writers);
    allwriter = dict();
    for wri in writers:
        allwriter[wri] = [];

    lines[1:];
    for line in lines:
        data = line.split(",");
        #print(data)
        word = data[0];
        if word == "না":
            continue;
        data = data[1:];
        #print(data);
        cnt = 0;
        for wri in writers:
            allwriter[wri].append((word,int(data[cnt])));
            cnt+=1;

    for wri in writers:
        #print(allwriter[wri][:10]);
        allwriter[wri] = getDect(allwriter[wri]);
        #print(wri+" "+str(allwriter[wri]));

    return allwriter;


def getTestVector():
    fw = open("test_data.txt","r",encoding="utf8");
    raw_text = fw.read();
    formated_text = formatText(raw_text);
    words = getWordList(formated_text);
    words = [word for word in words if len(word)>1];

    vectorB = dict();
    for word in words:
        vectorB[word] = 0;
    for word in words:
        vectorB[word] = vectorB[word]+1;

    return vectorB;


def dot(vecA,vecB):
    keysA = vecA.keys();
    keysB = vecB.keys();
    up = 0;
    downa = 0;
    downb = 0;

    for key in keysA:
        va = vecA.get(key,0);
        vb = vecB.get(key,0);
        up+= (va * vb);

    for key in keysA:
        downa+= (vecA[key]*vecA[key]);
    for key in keysA:
        vb = vecB.get(key,0);
        downb += (vb * vb);
    downa = math.sqrt(downa);
    downb = math.sqrt(downb);
    #print(up,downa,downb)
    return math.acos(up / (downb*downa))*180/math.pi;





def cosine():
    for flag in range(0,2):
        vecB = getTestVector();
        allwriter = makeWritersVectors(flag);
        keys = allwriter.keys();
        keys = sorted(keys);

        for wri in keys:
            vecA = allwriter[wri];
            res = dot(vecA,vecB);
            print(wri +" match "+str(res))
        print("")

    return ;


#makeWritersVectors();
cosine()

