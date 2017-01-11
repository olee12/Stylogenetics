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
        word_dect[key]= val;

    return word_dect;



def getFeaturesWords(flag):
    if flag==0:
        fw = open("./train data/Most frequent words.csv","r",encoding="utf8");
    elif flag==1:
        fw = open("./train data/Modified word frequency.csv","r",encoding="utf8");
    elif flag==2:
        fw = open("./train data/Distribution of some common Bengali words.csv","r",encoding="utf8");
    elif flag==3:
        fw = open("./train data/Spelling of particular words.csv","r",encoding="utf8");
    elif flag==4:
        fw = open("./train data/Bigrams.csv", "r", encoding="utf8");

    lines = fw.read().split("\n");
    fw.close();
    lines = lines[1:];
    feature_words = [];
    for line in lines:
        data = line.split(",");
        word = data[0];
        if word == "না":
            continue;
        word = word.strip();
        feature_words.append(word);
    return feature_words;


def getTestVector(feature_words,read_file):
    if len(feature_words[0].split(" ")) > 1:
        return getTestVector_two_word(feature_words,read_file);

    fw = open(read_file,"r",encoding="utf8");
    raw_text = fw.read();
    fw.close();
    formated_text = formatText(raw_text);
    words = getWordList(formated_text);
    words = [word for word in words if len(word)>1];
    words = [word for word in words if isEnglish(word)==False];
    vec = [];
    for word in feature_words:
        vec.append(words.count(word));
    return vec;


def getTestVector_two_word(feature_words,read_file):
    fw = open(read_file,"r",encoding="utf8");
    raw_text = fw.read();
    fw.close();
    formated_text = formatText(raw_text);
    words = getWordList(formated_text);
    words = [word for word in words if len(word)>1];
    words = [word for word in words if isEnglish(word)==False];
    myBigram = [];
    for i in range(0,len(words)-1):
        myBigram.append(words[i]+" "+words[i+1])
    vec = [];
    for word in feature_words:
        vec.append(myBigram.count(word));
    return vec;



def MakeVectorForSVM(read_file,feature_number,feature_words):
    vec = getTestVector(feature_words,read_file);
    return vec;

    #return tareq.count(writer);
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
    #print(tareq);
    return tareq.count(writer);



def MakeTrainDataForSVM(feature_number,feature_words):
    train_data = [];
    train_label = [];
    dir = "C:\\Users\\Tahmidolee\\Documents\\Project 300\\Stylogenetics\\Stylogenetics\\train_data\\";
    folders = os.listdir(dir);
    for writer in folders:
        if writer.find(".") != -1:
            continue;
        data_path = dir + writer + "\\";
        files = os.listdir(data_path);
        for file in files:
            fw = open(dir + writer + "\\" + file, "r", encoding="utf8");
            train_file = "train_data.txt";
            ft = open(train_file, "w", encoding="utf8");
            doc = fw.read();
            if len(getWordList(formatText(doc))) < 500:
                continue;
            ft.write(doc);
            ft.close();
            fw.close();
            # print(file);
            vec = MakeVectorForSVM(train_file,feature_number,feature_words)
            train_data.append(vec);
            train_label.append(writer);
            #print(vec);
            #print(writer);
            #print(len(vec));
    return train_data,train_label;


def MakeTestDataForSVM(feature_number,feature_words):
    test_data = [];
    test_label = [];
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
            train_file = "test_data.txt";
            ft = open(train_file, "w", encoding="utf8");
            doc = fw.read();
            if len(getWordList(formatText(doc))) < 500:
                continue;
            ft.write(doc);
            ft.close();
            fw.close();
            # print(file);
            vec = MakeVectorForSVM(train_file,feature_number,feature_words)
            test_data.append(vec);
            test_label.append(writer);
            #print(vec);
            #print(writer);
            #print(len(vec));
    return test_data,test_label;



def decisionTree():
    import pydotplus
    a,b,c,d = traing_test_data_set();
    for feature_number in range(1, 6):
        print("Feature Number : " + str(feature_number));
        train_data, train_label = a[feature_number - 1], b[feature_number - 1];
        test_data, test_label = c[feature_number - 1], d[feature_number - 1];
        from sklearn import tree
        clf = tree.DecisionTreeClassifier(criterion='entropy', min_samples_split=30, max_depth=15);
        clf.fit(train_data, train_label)
        with open("iris.dot", 'w') as f:
            f = tree.export_graphviz(clf, out_file=f)
        tot = len(test_label);
        cnt = 0;
        prediction = clf.predict(test_data);
        for i in range(0, len(test_data)):
            if clf.predict([test_data[i]])[0] != test_label[i]:
                # print(str(i)+str(clf.predict([test_data[i]]))+" "+str(test_label[i]));
                cnt += 1;
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import precision_score
        from sklearn.metrics import f1_score
        print("Complete for Feature :" + str(feature_number));
        print("Train Score : " + str(clf.score(train_data, train_label)));
        print("Total test set size : " + str(len(test_label)));
        print("Correct prediction : " + str(tot - cnt));
        print("Incorrect Prediction : " + str(cnt));
        print("Accuracy : " + str(accuracy_score(test_label, prediction) * 100.0))
        print("Precision : " + str(precision_score(test_label, prediction, average='weighted') * 100.0))
        print("F1 Score : " + str(f1_score(test_label, prediction, average='weighted') * 100.0))
        print("Error Rate : " + str(cnt / tot * 100.0));
        print("---------------------------------------\n");




def traing_test_data_set():
    train_data = list();
    train_label = list();
    test_data = list();
    test_label = list();
    for feature_number in range(1,6):
        print("Feature Number : "+str(feature_number));
        feature_words = getFeaturesWords(feature_number-1);
        a, b = MakeTrainDataForSVM(feature_number,feature_words);
        train_data.append(a);
        train_label.append(b);
        c, d = MakeTestDataForSVM(feature_number,feature_words);
        test_data.append(c);
        test_label.append(d);
    return train_data,train_label,test_data,test_label;



decisionTree();