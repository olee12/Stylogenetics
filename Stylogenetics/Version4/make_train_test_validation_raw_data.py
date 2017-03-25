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
import  random;
import math;


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


def write_files(writer,root_folder,files):
    make_sure_path_exists(root_folder+"\\"+writer);
    counter = 1;
    for file in files:
        write_path = root_folder+"\\"+writer+"\\"+writer+str(counter)+".doc";
        fw = open(write_path,"w",encoding="utf-8");
        fw.write(file);
        fw.close();
        counter+=1;


import os

def clean_path(path):
    path = path.replace('/',os.sep).replace('\\',os.sep)
    if os.sep == '\\' and '\\\\?\\' not in path:
        # fix for Windows 260 char limit
        relative_levels = len([directory for directory in path.split(os.sep) if directory == '..'])
        cwd = [directory for directory in os.getcwd().split(os.sep)] if ':' not in path else []
        path = '\\\\?\\' + os.sep.join(cwd[:len(cwd)-relative_levels]\
                         + [directory for directory in path.split(os.sep) if directory!=''][relative_levels:])
    return path

def writerInfo(atleast=500,train_path = "./Train Data",test_path="./Test data",validation_path="./Validation data"):
    dir = "All Data";
    folders = os.listdir(dir);
    total_file_coutn = 0;
    for writer in folders:
        if writer.find(".") != -1:
            continue;
        file_list = list();
        data_path = dir +"\\"+ writer ;
        files = os.listdir(data_path);
        file_count = 0;
        for file in files:
            file_path = data_path + "\\" + file;
            file_path = clean_path(file_path);
            fw = open(file_path, "r", encoding="utf8");
            train_file = "train_data.txt";
            ft = open(train_file, "w", encoding="utf8");
            doc = fw.read();
            if len(getWordList(formatText(doc))) < atleast:
                continue;
            file_count+=1;
            file_list.append(doc);
            #ft.write(doc);
            #ft.close();
            fw.close();
        print("writer : "+writer+" File_count : "+str(file_count));
        total_file_coutn+=file_count;
        random.shuffle(file_list);

        tot_size = len(file_list);
        train_size = math.floor(.7*len(file_list));
        train_files = file_list[:train_size];
        file_list = file_list[train_size+1:];
        validation_size = math.floor(.5*len(file_list));
        validation_files = file_list[:validation_size];
        test_files = file_list[validation_size+1:];
        write_files(writer,train_path,train_files);
        write_files(writer,validation_path,validation_files);
        write_files(writer,test_path,test_files);
    print("Total File Count : ",total_file_coutn);


writerInfo(300);