import time
import os
import shutil

def main():
    deleted_folders_count=0
    deleted_files_count=0
    path="PROJECT 99/pro"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_edge(root_folder):
                remove_folder(root_folder)
                deleted_folders_count+=1
                break
            
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds>=get_file_or_folder_edge(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count+=1
                    
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if seconds>=get_file_or_folder_edge(file_path):
                        remove_file(file_path)
                        deleted_files_count+=1
        
        else:
            if seconds>=get_file_or_folder_edge(path):
                remove_file(path)
                deleted_files_count+=1 
    
    else:
        print("The file does not exist")
        deleted_files_count+=1
    
    print("Total folders deleted:-"+deleted_folders_count)
    print("Total files deleted:-"+deleted_files_count)

def remove_folder(path):
    if not shutil.rmtree(path):
        print("The path has been removed successfully")
    
    else:
        print("Unable to remove the path")

def remove_file(path):
    if not os.remove(path):
        print("The path has been removed successfully")
    
    else:
        print("Unable to remove the path")

def get_file_or_folder_edge(path):
    ctime=os.stat(path).st_ctime
    return ctime

main()