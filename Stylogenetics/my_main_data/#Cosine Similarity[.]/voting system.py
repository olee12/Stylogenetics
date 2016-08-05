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
        word_dect[key]= val;

    return word_dect;

def makeWritersVectors(flag):
    if flag==1:
        fw = open("./train data/Common_word_changed_freq.csv","r",encoding="utf8");
    elif flag==0:
        fw = open("./train data/Filtered_one_word.csv","r",encoding="utf8");
    elif flag==2:
        fw = open("./train data/Freq_one_by_four_feature_words Phase 1.csv","r",encoding="utf8");
    elif flag==3:
        fw = open("./train data/Top_50_Freq_one_word.csv","r",encoding="utf8");
    elif flag==4:
        fw = open("./train data/Freq_two_word.csv", "r", encoding="utf8");

    lines = fw.read().split("\n");
    fw.close();
    head = lines[0];
    lines = lines[1:]
    writers=str(head[head.find(",")+1:]).split(",");
    #print(writers);
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
        #print(writers);
        for wri in writers:
            #print(wri);
            allwriter[wri].append((word,int(data[cnt])));
            cnt+=1;

    for wri in writers:
        #print(allwriter[wri][:10]);
        allwriter[wri] = getDect(allwriter[wri]);
        #print(wri+" "+str(allwriter[wri]));
    #print(" ");
    return allwriter;


def getTestVector_one_word():
    fw = open("test_data.txt","r",encoding="utf8");
    raw_text = fw.read();
    fw.close();
    formated_text = formatText(raw_text);
    #print(formated_text)
    words = getWordList(formated_text);
    words = [word for word in words if len(word)>1];
    words = [word for word in words if isEnglish(word)==False];

    vectorB = dict();
    for word in words:
        vectorB[word] = 0;
    for word in words:
        vectorB[word] = vectorB[word]+1;

    return vectorB;


def getTestVector_two_word():
    fw = open("test_data.txt","r",encoding="utf8");
    raw_text = fw.read();
    fw.close();
    formated_text = formatText(raw_text);
    #print(formated_text)
    words = getWordList(formated_text);
    words = [word for word in words if len(word)>1];
    words = [word for word in words if isEnglish(word)==False];
    myBigram = [];
    for i in range(0,len(words)-1):
        myBigram.append(words[i]+" "+words[i+1])
    vectorB = dict();
    for word in myBigram:
        vectorB[word] = 0;
    for word in myBigram:
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
        #print(key+" "+str(vb));
        downb += (vb * vb);
    downa = math.sqrt(downa);
    downb = math.sqrt(downb);
    if downa==0 or downb==0:
        return 100;
    return math.acos(up / (downb*downa))*180/math.pi;





def cosine(writer):
    tareq = [];
    for flag in range(0,4):
        vecB = getTestVector_one_word();
        allwriter = makeWritersVectors(flag);
        keys = allwriter.keys();
        keys = sorted(keys);
        result = dict();
        for wri in keys:
            vecA = allwriter[wri];
            res = dot(vecA,vecB);
            result[wri] = res;
            #print(wri +" match "+str(res))
        name = "";
        min = 10000;
        for wri in keys:
            if min>result[wri]:
                name = wri;
                min = result[wri];
        #print("\t\t"+name+" : "+str(min));
        tareq.append(name);

    #this is for bigram:
    for flag in range(4, 5):
        vecB = getTestVector_two_word();
        allwriter = makeWritersVectors(flag);
        keys = allwriter.keys();
        keys = sorted(keys);
        result = dict();
        for wri in keys:
            vecA = allwriter[wri];
            res = dot(vecA, vecB);
            result[wri] = res;
            # print(wri +" match "+str(res))
        name = "";
        min = 10000;
        for wri in keys:
            if min > result[wri]:
                name = wri;
                min = result[wri];
        #print("\t\t"+name+" : "+str(min));
        tareq.append(name);
    print(tareq);
    return tareq.count(writer);



def doItForAll():
    # makeWritersVectors();
    correct = 0;
    allresult = "Writer,5 error,4 error,3 error,2 error,1 error,5-tot,4-tot,3-tot,2-tot,1-tot\n";
    dir = "C:\\Users\\Tahmidolee\\Documents\\Project 300\\Stylogenetics\\Stylogenetics\\test_data\\";
    folders = os.listdir(dir);
    for writer in folders:
        if writer.find(".") != -1:
            continue;
        data_path = dir + writer + "\\";
        files = os.listdir(data_path);
        cnt = 0;
        sum = 0;
        error_list = [0, 0, 0, 0,0,0];
        for file in files:
            fw = open(dir + writer + "\\" + file, "r", encoding="utf8");
            ft = open("test_data.txt", "w", encoding="utf8");
            doc = fw.read();
            if len(getWordList(formatText(doc))) < 500:
                continue;
            ft.write(doc);
            ft.close();
            fw.close();
            # print(file);
            flag = cosine(writer)
            # print(flag);
            if flag >= 3:
                cnt+=1;
            else:
                print(file);
            sum+=1;

        print("\n\nWriter = " + writer);
        print("\nsucess 1: ");
        print(cnt/sum * 100.0);

    print("");



#print(cosine("MZI"));
doItForAll();