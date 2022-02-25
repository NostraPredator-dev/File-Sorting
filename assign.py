import os
import os
import shutil

path = input("Enter the path: ") + "/"

if os.path.exists(path):
    for file in os.listdir(path):
        tme = os.stat(path).st_ctime
        tme = tme/86400
        if tme >30:
            os.remove(path)
        name,ext = os.path.splitext(file)
        ext = ext[1:]

        if ext=='':
            continue
        if os.path.exists(path + ext):
            shutil.move(path + file, path + ext + '/' + file)
        else:
            os.makedirs(path + ext)
            shutil.move(path + file, path + ext + "/" + file)
else:
    print("Path does not exist")