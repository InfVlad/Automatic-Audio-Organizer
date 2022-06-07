'''
#----------------File handling-------------
#Rename - Change name of files in a directory
import os
os.chdir("C:\Projects\Stuff")

for file in os.listdir():
    # print(file)
    name, ext = os.path.splitext(file)
    name_2 = name[10:] #files just had long strings before the actual name
    # splitted = name.split(" ")

    # splitted_2 = splitted[3:-1]
    # splitted.remove("")
    # print(splitted)
    # if "" in splitted_2:
    #     splitted_2.remove("")
    # new_name = "".join(splitted)
    new_name = f"{new_name}{ext}"
    print(new_name)
    os.rename(file, new_name)
'''
import os
import shutil
root = "D:\Weeb Shit\JDownloader"
mp3_stuff = "D:\Weeb Shit\Music"
no_mp3_stuff = "D:\Weeb Shit\Music/no mp3"
extensions = [".ogg",".aac",".m4a"]
ext_and_bitrate = ["(128kbit_AAC)","(128kbit_Opus)","(152kbit_Opus)","(160kbit_Opus)","(256kbit_Opus)","(192kbit_Opus)","(192kbit_AAC)"]
file_renamed = False
x = 0
for path, subdirs, files in os.walk(root):
    for file in files:
        name, ext = os.path.splitext(file)
        os.chdir(path)
        if ext in extensions or ext ==".mp3":
            splitted = name.split(" ")
            if splitted[-1] in ext_and_bitrate:
                splitted.remove(splitted[-1])
            new_name = " ".join(splitted)
            new_name = f"{new_name}{ext}"
            os.rename(file, new_name)
            file_renamed = True
            x += 1
if file_renamed:
    print(f"{x} Files Renamed Successfully")
else:
    print("No Files Renamed")
y = 0
file_moved = False
for path, subdirs, files in os.walk(root):
    for file in files:
        name, ext = os.path.splitext(file)
        if ext in extensions:
            # print(path)
            source = path + "\\" + file
            destination = no_mp3_stuff + "\\" + file
            shutil.move(source, destination)
            y += 1
            file_moved = True
        elif ext == ".mp3":
            source = path + "\\" + file
            destination = mp3_stuff + "\\" + file
            shutil.move(source, destination)
            y += 1
            file_moved = True
if file_moved:
    print(f"{y} Files Moved Successfully")
else:
    print("No Files Moved")

# folders_deleted = False
# z = 0
# folders = list(os.walk(root))[1:]
# for folder in folders[::-1]:
#     # folder example: ('FOLDER/3', [], ['file']) --- name of folder, subfolders and files inside
#     if not folder[2]: #if no files, remove folder
#         os.rmdir(folder[0])
#         folders_deleted = True
#         z+=1
# if folders_deleted:
#     print(f"{z} Empty Folders Deleted Successfully")
# else:
#     print("No Folders Deleted")