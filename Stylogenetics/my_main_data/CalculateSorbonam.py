

import os

import errno
from nltk.tokenize import  word_tokenize


writers = ['Emon Jubayer','Hasan Mahbub','Kandari Athorbo','MZI','Nir Shondhani','Tareque Anu']


def make_sure_path_exists():
    try:
        for item in writers:
            os.makedirs("./#Sorbonam[.]/"+item+"/")
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            pass

def calculateSorbonam():
    for writemItem in writers:
        fileofWriters = os.listdir("./" + writemItem + "/")
        for fileItem in fileofWriters:
            if fileItem.find("Normal") != -1 or fileItem.find("data") != -1:
                inputFile = open(r"./" + writemItem +"/"+ fileItem, "rU", encoding="UTF-8")
                reader = inputFile.read()
                Sorbonam = open(r"./Partial Data[.]/sorbonam/sarbonam_one word.txt", "r", encoding="UTF-8").read()
                Sorbonam1 = open(r"./Partial Data[.]/sorbonam/sarbonam_two word.txt", "r", encoding="UTF-8").read()
                Sorbonam1 = Sorbonam1.replace("*", "")
                Sorbonam = Sorbonam + "\n" + Sorbonam1
                Sorbonam = Sorbonam.replace("*", "")
                Sorbonam = Sorbonam.split("\n")
                Sorbonam = [s.strip() for s in Sorbonam];

                # print(Sorbonam)
                mapper = dict()
                for key in Sorbonam:
                    mapper[key] = 0
                tokens = word_tokenize(reader)
                for words in Sorbonam:
                    mapper[words] = tokens.count(words)
                # print(mapper.keys())
                # print(mapper.values())
                lista = []
                writingString = "Sorbonam,Frequency\n"
                writeFile = open("#Sorbonam[.]/" + writemItem  + "/"+ fileItem[:len(fileItem)-4] + "[sorbonam].csv", "w", encoding="utf-8")
                for item in mapper.keys():
                    lista.append((mapper[item], item))
                for item in reversed(sorted(lista)):
                    writingString += item[1] + "," + str(item[0]) + '\n'
                writeFile.write(writingString)
                writeFile.close()
                # print(tokens[:100])

make_sure_path_exists()
calculateSorbonam()






