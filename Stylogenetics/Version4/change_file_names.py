import os;

def clean_path(path):
    path = path.replace('/',os.sep).replace('\\',os.sep)
    if os.sep == '\\' and '\\\\?\\' not in path:
        # fix for Windows 260 char limit
        relative_levels = len([directory for directory in path.split(os.sep) if directory == '..'])
        cwd = [directory for directory in os.getcwd().split(os.sep)] if ':' not in path else []
        path = '\\\\?\\' + os.sep.join(cwd[:len(cwd)-relative_levels]\
                         + [directory for directory in path.split(os.sep) if directory!=''][relative_levels:])
    return path


def remane_all_file_in_folder(root = "All Data"):
    root_path = clean_path(root);
    print(root_path);
    writers = os.listdir(root_path);
    for writer in writers:
        folder_path = root_path + "\\"+writer;
        folder_path = clean_path(folder_path);
        file_list = os.listdir(folder_path);
        new_files = list();
        file_count = 9000;
        for file in file_list:
            file_path = folder_path + "\\" + file;
            file_path = clean_path(file_path);
            fw = open(file_path,"r",encoding='utf-8');
            data_in_file = fw.read();
            fw.close();
            new_name = writer + str(file_count)+".doc";
            new_file_path = folder_path+"\\"+new_name;
            new_file_path = clean_path(new_file_path);
            fw = open(new_file_path,"w",encoding='utf-8');
            fw.write(data_in_file);
            file_count+=1;
            fw.close();
            os.remove(file_path);
    return ;

remane_all_file_in_folder();