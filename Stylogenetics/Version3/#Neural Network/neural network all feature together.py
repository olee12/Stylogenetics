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

def neuralNetwork():
    import pydotplus
    a,b,c,d,e,f = traing_test_data_set();
    for feature_number in range(1, 2):
        print("Feature Number : " + str(feature_number));
        train_data, train_label = a[feature_number - 1], b[feature_number - 1];
        test_data, test_label = c[feature_number - 1], d[feature_number - 1];
        validation_data,validation_label = e[feature_number-1],f[feature_number-1];
        from sklearn.neural_network import MLPClassifier
        clf = MLPClassifier(alpha=1, hidden_layer_sizes=(100,), random_state=1, activation='logistic', max_iter=1000);
        clf.fit(train_data, train_label)

        tot = len(test_label);
        cnt = 0;
        prediction = clf.predict(test_data);
        for i in range(0, len(test_data)):
            if clf.predict([test_data[i]])[0] != test_label[i]:
                print(str(i)+str(clf.predict([test_data[i]]))+" "+str(test_label[i]));
                cnt += 1;
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import precision_score
        from sklearn.metrics import f1_score
        print("Complete for Feature :" + str(feature_number));
        print("Train data set size : " + str(len(train_data)));
        print("Train Score : " + str(clf.score(train_data, train_label)));
        print("Total test set size : " + str(len(test_label)));
        print("Correct prediction : " + str(tot - cnt));
        print("Incorrect Prediction : " + str(cnt));
        print("Accuracy : " + str(accuracy_score(test_label, prediction) * 100.0))
        print("Precision : " + str(precision_score(test_label, prediction, average='weighted') * 100.0))
        print("F1 Score : " + str(f1_score(test_label, prediction, average='weighted') * 100.0))
        print("Error Rate : " + str(cnt / tot * 100.0));
        print("---------------------------------------\n");
        test_label = validation_label;
        test_data = validation_data;
        tot = len(test_label);
        cnt = 0;
        prediction = clf.predict(test_data);
        for i in range(0, len(test_data)):
            if clf.predict([test_data[i]])[0] != test_label[i]:
                print(str(i)+str(clf.predict([test_data[i]]))+" "+str(test_label[i]));
                cnt += 1;
        print("Total validation set size : " + str(len(test_label)));
        print("Correct prediction : " + str(tot - cnt));
        print("Incorrect Prediction : " + str(cnt));
        print("Accuracy : " + str(accuracy_score(test_label, prediction) * 100.0))
        print("Precision : " + str(precision_score(test_label, prediction, average='weighted') * 100.0))
        print("F1 Score : " + str(f1_score(test_label, prediction, average='weighted') * 100.0))
        print("Error Rate : " + str(cnt / tot * 100.0));
        print("---------------------------------------\n");

def neuralNetworkHiddenLayerNumberAnalysis():
    import pydotplus
    a,b,c,d,e,f = traing_test_data_set();
    for feature_number in range(1, 2):
        print("Feature Number : " + str(feature_number));
        train_data, train_label = a[feature_number - 1], b[feature_number - 1];
        test_data, test_label = c[feature_number - 1], d[feature_number - 1];
        validation_data,validation_label = e[feature_number-1],f[feature_number-1];
        print("Train data set size : " + str(len(train_data)));
        print("Test set size : " + str(len(test_label)));
        print("Validation set size : " + str(len(validation_label)));
        print("------------------------------------------------");
        alphalist = [.00001, .00003, .0001, .0003, .001, .003, .01, .03, 1, 10]
        from sklearn.neural_network import MLPClassifier
        for new_alpha in alphalist:
            hiddenLayerAnalysisResult = "Number of node in 1st hidden layer,train score,validation score,test score,iterations\n";
            for hiddenNode in range(5,400,5):
                clf = MLPClassifier(alpha=new_alpha,tol = 1e-5, hidden_layer_sizes=(hiddenNode,), random_state=1, activation='logistic', max_iter=1000);
                clf.fit(train_data, train_label)

                tot = len(test_label);
                cnt = 0;
                prediction = clf.predict(test_data);
                for i in range(0, len(test_data)):
                    if prediction[i] != test_label[i]:
                        #print(str(i)+str(clf.predict([test_data[i]]))+" "+str(test_label[i]));
                        cnt += 1;
                from sklearn.metrics import accuracy_score
                from sklearn.metrics import precision_score
                from sklearn.metrics import f1_score

                print("Number of node in first hidden layer :" + str(hiddenNode));
                print("Train Score : " + str(clf.score(train_data, train_label)));
                train_score = str(clf.score(train_data, train_label));
                test_score = str(accuracy_score(test_label, prediction) * 100.0);
                print("On test set");
                print("Correct prediction : " + str(tot - cnt));
                print("Incorrect Prediction : " + str(cnt));
                print("Accuracy : " + str(accuracy_score(test_label, prediction) * 100.0))
                print("Precision : " + str(precision_score(test_label, prediction, average='weighted') * 100.0))
                print("F1 Score : " + str(f1_score(test_label, prediction, average='weighted') * 100.0))
                print("Error Rate : " + str(cnt / tot * 100.0));
                print("---------------------------------------\n");
                tot = len(test_label);
                cnt = 0;
                prediction = clf.predict(validation_data);

                for i in range(0, len(validation_data)):
                    if clf.predict([validation_data[i]])[0] != validation_label[i]:
                        #print(str(i)+str(clf.predict([test_data[i]]))+" "+str(test_label[i]));
                        cnt += 1;
                print("On validation set");
                validation_score = str(accuracy_score(validation_label, prediction) * 100.0);
                print("Correct prediction : " + str(tot - cnt));
                print("Incorrect Prediction : " + str(cnt));
                print("Accuracy : " + str(accuracy_score(validation_label, prediction) * 100.0))
                print("Precision : " + str(precision_score(validation_label, prediction, average='weighted') * 100.0))
                print("F1 Score : " + str(f1_score(validation_label, prediction, average='weighted') * 100.0))
                print("Error Rate : " + str(cnt / tot * 100.0));
                print("---------------------------------------\n");
                hiddenLayerAnalysisResult+= str(hiddenNode)+","+train_score+","+validation_score+","+test_score+","+str(clf.n_iter_)+"\n";

            file_name = "hiddenLayerAnalysisResult " + " With alpha = [ " + str(new_alpha) + "] .csv";
            fw = open(file_name, "w", encoding="utf-8");
            fw.write(hiddenLayerAnalysisResult);
            fw.close();


def neuralNetworkIteration():
    import pydotplus
    a,b,c,d,e,f = traing_test_data_set();
    alphalist = [.00001,.00003,.0001,.0003,.001,.003,.01,.03,1,10]
    for feature_number in range(1, 2):

        print("Feature Number : " + str(feature_number));
        train_data, train_label = a[feature_number - 1], b[feature_number - 1];
        test_data, test_label = c[feature_number - 1], d[feature_number - 1];
        validation_data,validation_label = e[feature_number-1],f[feature_number-1];
        for new_alpha in alphalist:
            iteration_output = "Iteration,Training Error,Validation Error\n";
            from sklearn.neural_network import MLPClassifier
            clf = MLPClassifier(alpha=new_alpha, hidden_layer_sizes=(200,), random_state=1, activation='logistic',
                                warm_start=True,max_iter=1);
            for iteration in range(1,500):
                clf.fit(train_data, train_label)
                prediction = clf.predict(validation_data);
                from sklearn.metrics import accuracy_score
                iteration_output+=str(str(iteration) +","+ str(100-clf.score(train_data, train_label)*100.0)+","+str(100-accuracy_score(validation_label, prediction) * 100.0));
                iteration_output+="\n";
                print(str(str(iteration) +","+ str(100-clf.score(train_data, train_label)*100.0)+","+str(100-accuracy_score(validation_label, prediction) * 100.0)))
            file_name = "For All Feature. Alpha = "+str(new_alpha)+" "+" Iteration data"+".csv";
            print(file_name);
            datafile = open(file_name,"w",encoding="utf-8");
            datafile.write(iteration_output);
            datafile.close();

def neuralNetworkIterationLogistic():
    import pydotplus
    a,b,c,d,e,f = traing_test_data_set();
    for feature_number in range(1, 6):
        iteration_output = "Iteration,Training Error,Validation Error\n";
        print("Feature Number : " + str(feature_number));
        train_data, train_label = a[feature_number - 1], b[feature_number - 1];
        test_data, test_label = c[feature_number - 1], d[feature_number - 1];
        validation_data,validation_label = e[feature_number-1],f[feature_number-1];
        from sklearn.neural_network import MLPClassifier
        clf = MLPClassifier(alpha=1, hidden_layer_sizes=(15,), random_state=1, activation='logistic',
                            warm_start=True,max_iter=1);
        for iteration in range(1,350):
            clf.fit(train_data, train_label)
            tot = len(validation_data);
            cnt = 0;
            prediction = clf.predict(validation_data);
            for i in range(0, len(validation_data)):
                if clf.predict([validation_data[i]])[0] != validation_label[i]:
                    # print(str(i)+str(clf.predict([test_data[i]]))+" "+str(test_label[i]));
                    cnt += 1;
            from sklearn.metrics import accuracy_score
            from sklearn.metrics import precision_score
            from sklearn.metrics import f1_score
            iteration_output+=str(str(iteration) +","+ str(100-clf.score(train_data, train_label)*100.0)+","+str(100-accuracy_score(validation_label, prediction) * 100.0));
            iteration_output+="\n";
            print(str(str(iteration) +","+ str(100-clf.score(train_data, train_label)*100.0)+","+str(100-accuracy_score(validation_label, prediction) * 100.0)))
        file_name = "Feature No "+str(feature_number)+" Iteration data"+".csv";
        print(file_name);
        datafile = open(file_name,"w",encoding="utf-8");
        datafile.write(iteration_output);
        datafile.close();

def traing_test_data_set():
    train_data = list();
    train_label = list();
    test_data = list();
    test_label = list();
    validation_data = list();
    validation_label = list();
    total_word_set = set();
    for feature_number in range(1,5):
        print("Feature Number : " + str(feature_number));
        feature_words = getFeaturesWords(feature_number - 1);
        for word in feature_words:
            total_word_set.add(word);
    print("total feature vec size : "+str(len(total_word_set)));
    #print("Feature Number : "+str(feature_number));
    feature_words = list(total_word_set);

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

def traing_test_data_set_with_bi_grams():
    train_data = list();
    train_label = list();
    test_data = list();
    test_label = list();
    validation_data = list();
    validation_label = list();
    total_word_set = set();
    b_grams = list();
    for feature_number in range(5,6):
        b_grams = getFeaturesWords(feature_number-1);

    for feature_number in range(1,5):
        print("Feature Number : " + str(feature_number));
        feature_words = getFeaturesWords(feature_number - 1);
        for word in feature_words:
            total_word_set.add(word);
    print("total feature vec size : "+str(len(total_word_set)));
    #print("Feature Number : "+str(feature_number));
    feature_words = list(total_word_set);

    a, b = MakeTrainDataForSVM(feature_number,feature_words);
    a_bi, b_bi = MakeTrainDataForSVM(feature_number,b_grams);
    for i in range(0,len(a_bi)):
        a[i].extend(a_bi[i]);
    train_data.append(a);
    train_label.append(b);
    c, d = MakeTestDataForSVM(feature_number,feature_words);
    c_bi, d_bi = MakeTestDataForSVM(feature_number, b_grams);
    for i in range(0, len(c_bi)):
        c[i].extend(c_bi[i]);
    test_data.append(c);
    test_label.append(d);
    e, f = MakeValidationDataForSVM(feature_number,feature_words);
    e_bi, f_bi = MakeValidationDataForSVM(feature_number, b_grams);
    for i in range(0, len(e_bi)):
        e[i].extend(e_bi[i]);
    validation_data.append(e);
    validation_label.append(f);
    return train_data,train_label,test_data,test_label,validation_data,validation_label;


a,b,c,d,e,f = traing_test_data_set_with_bi_grams();
neuralNetworkIteration();