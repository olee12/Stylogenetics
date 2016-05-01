import os;
print(len("| মুহম্মদ জাফর ইকবাল"))
root = "./"

dirlist = os.listdir(root);
for dir in dirlist:
    if dir.find(".")!=-1 :
        continue;
    nlist = os.listdir(root + dir);
    for file in nlist:
        #if file[0] != "d":
            #continue;
        fw = open(root + dir +"/"+ file, "r", encoding="utf8");
        text = fw.read()
        if text.find(u"এডমিন নোট") != -1:
            print(file);
            #text = text.replace(u"Click This Link","")
            pos = text.find("সর্বশেষ এডিট");
            text = text[:pos];
            fw.close();
            fw = open(root + dir +"/"+ file, "w", encoding="utf8");
            print(root + dir +"/"+ file)
            fw.write(text);
            fw.close();



text = "Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link "
text = text.replace("Click"," ");
print(text);