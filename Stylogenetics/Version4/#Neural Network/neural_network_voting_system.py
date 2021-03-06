from sklearn import svm;
import os
from nltk.tokenize import word_tokenize
import nltk;
from nltk.probability import FreqDist;
import errno
import math;
biram_file = open("./Features/biram.txt","r",encoding="utf8")
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
        fw = open("./Features/Most frequent words.csv","r",encoding="utf8");
    elif flag==1:
        fw = open("./Features/Modified word frequency.csv","r",encoding="utf8");
    elif flag==2:
        fw = open("./Features/Distribution of some common Bengali words.csv","r",encoding="utf8");
    elif flag==3:
        fw = open("./Features/Spelling of particular words.csv","r",encoding="utf8");
    elif flag==4:
        fw = open("./Features/Bigrams.csv", "r", encoding="utf8");

    lines = fw.read().split("\n");
    fw.close();

    feature_words = [];
    for line in lines:
        word = line;
        word = word.strip();
        if len(word)>=1:
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


def MakeTrainDataForSVM(feature_number,feature_words,atleast=300):
    train_data = [];
    train_label = [];
    dir = "C:\\Users\\Tahmidolee\\Documents\\Project 300\\Stylogenetics\\Stylogenetics\\Version3\\Train Data\\";
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
            if len(getWordList(formatText(doc))) < atleast:
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


def MakeTestDataForSVM(feature_number,feature_words,atleast = 300):
    test_data = [];
    test_label = [];
    dir = "C:\\Users\\Tahmidolee\\Documents\\Project 300\\Stylogenetics\\Stylogenetics\\Version3\\Test Data\\";
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
            if len(getWordList(formatText(doc))) < atleast:
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


def MakeValidationDataForSVM(feature_number,feature_words,atleast = 300):
    test_data = [];
    test_label = [];
    dir = "C:\\Users\\Tahmidolee\\Documents\\Project 300\\Stylogenetics\\Stylogenetics\\Version3\\Validation Data\\";
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
            if len(getWordList(formatText(doc))) < atleast:
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

def most_common(lst):
    return max(set(lst), key=lst.count)

def neural_network_voting_systemLogistic():
    import pydotplus
    a,b,c,d,e,f = traing_test_data_set();
    iterations = [75, 60, 90, 95, 95];
    voting_pred = list();
    for i in range(0, len(d[0])):
        voting_pred.append([]);
    import random
    for feature_number in range(1, 6):
        print("Feature Number : " + str(feature_number));
        train_data, train_label = a[feature_number - 1], b[feature_number - 1];
        test_data, test_label = c[feature_number - 1], d[feature_number - 1];
        # use feature scaling for rbf kernel
        # from sklearn.preprocessing import StandardScaler
        # scaler = StandardScaler();
        # scaler.fit(train_data);
        # train_data = scaler.transform(train_data);
        # test_data = scaler.transform(test_data);
        #rnd = list(zip(train_data,train_label));
        #random.shuffle(rnd);
        #train_data, train_label = zip(*rnd)
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler();
        scaler.fit(train_data);
        train_data = scaler.transform(train_data);
        test_data = scaler.transform(test_data);
        from sklearn.neural_network import MLPClassifier
        clf = MLPClassifier(alpha=1, hidden_layer_sizes=(15,), random_state=1, activation='logistic',max_iter =1000,early_stopping=False)
        clf.fit(train_data, train_label)
        tot = len(test_label);
        cnt = 0;
        print(clf.n_iter_);
        for i in range(0, len(test_data)):
            voting_pred[i].append(clf.predict([test_data[i]])[0]);

    tot = len(test_label);
    cnt = 0;
    prediction = list();
    for i in range(0, len(test_data)):
        prediction.append(most_common(voting_pred[i]));
        if prediction[i] != test_label[i]:
            print(str(i) + " " + str(prediction[i]) + " " + str(test_label[i]));
            cnt += 1;
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import f1_score
    print("Complete for Voting system :");
    print("Total test set size : " + str(len(test_label)));
    print("Correct prediction : " + str(tot - cnt));
    print("Incorrect Prediction : " + str(cnt));
    print("Accuracy : " + str(accuracy_score(test_label, prediction) * 100.0))
    print("Precision : " + str(precision_score(test_label, prediction, average='weighted') * 100.0))
    print("F1 Score : " + str(f1_score(test_label, prediction, average='weighted') * 100.0))
    print("Error Rate : " + str(cnt / tot * 100.0));
    print("---------------------------------------\n");



def neural_network_voting_systemRelu():
    import pydotplus
    iterations = [75, 60, 90, 95, 95];
    a, b, c, d, e, f = traing_test_data_set();
    voting_pred = list();
    for i in range(0, len(d[0])):
        voting_pred.append([]);
    import random
    for feature_number in range(1, 6):
        print("Feature Number : " + str(feature_number));
        train_data, train_label = a[feature_number - 1], b[feature_number - 1];
        test_data, test_label = c[feature_number - 1], d[feature_number - 1];
        #from sklearn.preprocessing import StandardScaler
        #scaler = StandardScaler();
        #scaler.fit(train_data);
        #train_data = scaler.transform(train_data);
        #test_data = scaler.transform(test_data);
        #rnd = list(zip(train_data,train_label));
        #random.shuffle(rnd);
        #train_data, train_label = zip(*rnd)
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler();
        scaler.fit(train_data);
        train_data = scaler.transform(train_data);
        test_data = scaler.transform(test_data);
        from sklearn.neural_network import MLPClassifier
        clf = MLPClassifier(alpha=1, hidden_layer_sizes=(10,), random_state=1, activation='relu',max_iter =500,early_stopping=False)
        clf.fit(train_data, train_label)
        tot = len(test_label);
        cnt = 0;
        print(clf.n_iter_);
        for i in range(0, len(test_data)):
            voting_pred[i].append(clf.predict([test_data[i]])[0]);

    tot = len(test_label);
    cnt = 0;
    prediction = list();
    for i in range(0, len(test_data)):
        prediction.append(most_common(voting_pred[i]));
        if prediction[i] != test_label[i]:
            print(str(i) + " " + str(prediction[i]) + " " + str(test_label[i]));
            cnt += 1;
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import f1_score
    print("Complete for Voting system :");
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
    validation_data = list();
    validation_label = list();
    for feature_number in range(1,6):
        print("Feature Number : "+str(feature_number));
        feature_words = getFeaturesWords(feature_number-1);
        a, b = MakeTrainDataForSVM(feature_number,feature_words);
        train_data.append(a);
        train_label.append(b);
        c, d = MakeTestDataForSVM(feature_number,feature_words);
        test_data.append(c);
        test_label.append(d);
        e, f = MakeValidationDataForSVM(feature_number,feature_words);
        validation_data.append(e);
        validation_label.append(f);
    return train_data,train_label,test_data,test_label,validation_data,validation_label;



neural_network_voting_systemLogistic();
