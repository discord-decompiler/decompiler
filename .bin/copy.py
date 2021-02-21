import shutil
import os
import configparser
shutil.rmtree('.temp/boostrap', ignore_errors=True)
shutil.rmtree('.temp/app', ignore_errors=True)

config = configparser.ConfigParser()
config.read('settings.ini')
settings = config['settings']
discordpath = settings['discordpath']
if discordpath == "default":
    print('input discord path')
    discordpath = input()
    settings["discordpath"] = discordpath
    config.set('settings','discordpath',discordpath)
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)
try:
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
settings["discordpath"] = discordpath
try:
    os.mkdir("../src")
    os.mkdir("../src/app")
    os.mkdir("../src/boostrap")
except:
    pass
os.system("python unpack.py")
