import shutil
import os
discordpath = None #smh 
shutil.rmtree('.temp/boostrap', ignore_errors=True)
shutil.rmtree('.temp/app', ignore_errors=True)
shutil.rmtree('.temp/modules', ignore_errors=True)


if discordpath == None:
    print('input discord path')
    discordpath = input()
try:
    shutil.copy(f"{discordpath}/resources/app.asar ", '../.temp/boostrap/app.asar')
    try:
        os.mkdir("../.temp/boostrap")
        try:
            shutil.copy(f"{discordpath}/resources/app.asar ", '../.temp/boostrap/app.asar')
        except:
            pass
    except:
        pass
except:
    os.remove("../.temp/boostrap/app.asar")
    shutil.copy(f"{discordpath}/resources/app.asar ", '../.temp/boostrap/app.asar')
dirlist = os.listdir(f"{discordpath}/modules")
for dirs in dirlist:
    if "desktop_core" in dirs:
        path = os.path.join(f"{discordpath}","modules",dirs,"discord_desktop_core")
        try:
            os.removedirs("../.temp/app/")
        except:
            try:
                os.mkdir("../.temp/app/")
            except:
                pass
        try:
            shutil.copytree(path, "../.temp/app/")
        except:
            try:
                os.removedirs("../.temp/app/")
                shutil.copytree(path, "../.temp/app/")
            except:
                try:
                    os.removedirs("../.temp/app/")
                except:
                    try:
                        os.removedirs("../.temp/app/")
                    except:
                        pass

try:
    path = os.path.join(f"{discordpath}","modules")
    shutil.copytree(path, "../.temp/modules/")
    os.removedirs("../.temp/modules/")
except:
    try:
        os.mkdir("../.temp/modules/")
    except:
        pass
    try:
        shutil.copytree(path, "../.temp/modules/")
    except:
        try:
            os.removedirs("../.temp/modules/")
            shutil.copytree(path, "../.temp/modules/")
        except:
            try:
                os.removedirs("../.temp/modules/")
            except:
                try:
                    os.removedirs("../.temp/modules/")
                except:
                    pass

try:
    os.mkdir("../src")
    os.mkdir("../src/app")
    os.mkdir("../src/boostrap")
except:
    pass
os.system("python unpack.py")
