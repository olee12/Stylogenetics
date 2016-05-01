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

def MakeFolderNormal(folder):
    """only give the folder name in current dir."""

    folder_name = "./" + folder + "/"
    file_list = os.listdir(folder_name)
    mainText = ""
    for file in file_list:
        if (file.find("Normal") != -1) or (file=="data.doc") :
            continue;
        tmp_text = "";
        fw = open(folder_name + file, "r", encoding="utf-8")
        print(file)
        text = fw.read();
        #print(text);
        formated_text = formatText(text);
        mainText += formated_text
        mainText += "\n\n\n\n\n";
        tmp_text += formated_text;
        fw.close();
        ## creating new fromated file
        fw = open(folder_name + "Normal_" + file, "w", encoding="utf-8")
        fw.write(tmp_text);
        fw.close();

    fw = open(folder_name + "data.doc", "w", encoding="utf8");
    fw.write(mainText)



MakeFolderNormal("Tareque Anu")
