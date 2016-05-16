

import os

import errno
from nltk.tokenize import  word_tokenize


writers = ['Emon Jubayer','Hasan Mahbub','Kandari Athorbo','MZI','Nir Shondhani','Tareque Anu']


def make_sure_path_exists():
    try:
        for item in writers:
            os.makedirs("./#Obboy[.]/"+item+"/")
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            pass

def calculateObboy():
    for writemItem in writers:
        fileofWriters = os.listdir("./" + writemItem + "/")
        for fileItem in fileofWriters:
            if fileItem.find("Normal") != -1 or fileItem.find("data") != -1:
                inputFile = open(r"./" + writemItem +"/"+ fileItem, "rU", encoding="UTF-8")
                reader = inputFile.read()
                obboy = open(r"./Partial Data[.]/abboy/abboy_one word.txt", "r", encoding="UTF-8").read()
                obboy1 = open(r"./Partial Data[.]/abboy/abboy_two word.txt", "r", encoding="UTF-8").read()
                obboy1 = obboy1.replace("*", "")
                obboy = obboy + "\n" + obboy1
                obboy = obboy.replace("*", "")
                obboy = obboy.split("\n")
                # print(obboy)
                mapper = dict()
                for key in obboy:
                    mapper[key] = 0
                tokens = word_tokenize(reader)
                for words in obboy:
                    mapper[words] = tokens.count(words)
                if writemItem=="Tareque Anu":
                    print(fileItem+" "+str(mapper["ও"]))
                # print(mapper.keys())
                # print(mapper.values())
                lista = []
                writingString = "Obboy,Frequency\n"
                writeFile = open("#Obboy[.]/" + writemItem  + "/"+ fileItem[:len(fileItem)-4] + "[obboy].csv", "w", encoding="utf-8")
                for item in mapper.keys():
                    lista.append((mapper[item], item))
                for item in reversed(sorted(lista)):
                    writingString += item[1] + "," + str(item[0]) + '\n'
                writeFile.write(writingString)
                writeFile.close()
                # print(tokens[:100])

make_sure_path_exists()
calculateObboy()






