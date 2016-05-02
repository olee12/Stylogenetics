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
        if text.find("eval(unescape('%64%6f%63%75%6d%65%6e%74%2e%77%72%69%74%65%28%27%3c%61%20%68%72%65%66%3d%22%6d%61%69%6c%74%6f%3a%75%6e%69%72%65%73%6f%75%72%63%65%73%40%67%6d%61%69%6c%2e%63%6f%6d%22%3e%75%6e%69%72%65%73%6f%75%72%63%65%73%40%67%6d%61%69%6c%2e%63%6f%6d%3c%2f%61%3e%27%29%3b'))") != -1:
            print(file);
            text = text.replace("eval(unescape('%64%6f%63%75%6d%65%6e%74%2e%77%72%69%74%65%28%27%3c%61%20%68%72%65%66%3d%22%6d%61%69%6c%74%6f%3a%75%6e%69%72%65%73%6f%75%72%63%65%73%40%67%6d%61%69%6c%2e%63%6f%6d%22%3e%75%6e%69%72%65%73%6f%75%72%63%65%73%40%67%6d%61%69%6c%2e%63%6f%6d%3c%2f%61%3e%27%29%3b'))","")
            #pos = text.find("eval ( unescape (  '  % 64 % 6f % 63 % 75 % 6d % 65 % 6e % 74 % 2e % 77 % 72 % 69 % 74 % 65 % 28 % 27 % 3c % 61 % 20 % 68 % 72 % 65 % 66 % 3d % 22 % 6d % 61 % 69 % 6c % 74 % 6f % 3a % 75 % 6e % 69 % 72 % 65 % 73 % 6f % 75 % 72 % 63 % 65 % 73 % 40 % 67 % 6d % 61 % 69 % 6c % 2e % 63 % 6f % 6d % 22 % 3e % 75 % 6e % 69 % 72 % 65 % 73 % 6f % 75 % 72 % 63 % 65 % 73 % 40 % 67 % 6d % 61 % 69 % 6c % 2e % 63 % 6f % 6d % 3c % 2f % 61 % 3e % 27 % 29 % 3b '  )  )");
            #text = text[:pos];
            fw.close();
            fw = open(root + dir +"/"+ file, "w", encoding="utf8");
            print(root + dir +"/"+ file)
            fw.write(text);
            fw.close();



text = "Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link Click This Link "
text = text.replace("Click"," ");
print(text);