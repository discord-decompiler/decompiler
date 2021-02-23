import os
import shutil
import time
path = os.getcwd() 
p = os.path.abspath(os.path.join(path, os.pardir))
try:
    os.mkdir("../build/")
except:
    pass

print(p)
os.system(f"electron-packager {p}/src/boostrap discord --overwrite ")

shutil.copytree(path, "../.temp/modules/")
dirlist = os.listdir("../.temp/modules/")
for dirs in dirlist:
    if "desktop_core" in dirs:
        path = os.path.join(f"../.temp/modules/",dirs,"discord_desktop_core")
        shutil.copytree("../build/.temp", "../.temp/modules/")

shutil.copytree(path, "../.temp/app/")
os.system(f'asar pack {p}/src/app {p}/build/.temp')
print('pack ok ')