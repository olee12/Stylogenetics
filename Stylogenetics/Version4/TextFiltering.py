import os;
print(len("| মুহম্মদ জাফর ইকবাল"))
root = "./"

writers = os.listdir("./");
for writer in writers:
    if writer.find(".")!=-1 :
        continue;
    folder_path = "./"+writer;
    files = os.listdir(folder_path);
    for file in files:
        file_path = folder_path + "\\" + file;
        fw = open(file_path,'r',encoding='utf-8');
        mystring = str(fw.read());
        if mystring.find("সর্বশেষ এডিট") != -1:
            print(file+str(mystring.find("সর্বশেষ এডিট"))+" "+mystring[mystring.find("সর্বশেষ এডিট"):]);
            mystring = mystring[:mystring.find("সর্বশেষ এডিট")];
            fw = open(file_path,"w",encoding='utf-8');
            fw.truncate();
            fw.write(mystring);
            fw.close();



