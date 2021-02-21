import os
path = os.getcwd() 
p = os.path.abspath(os.path.join(path, os.pardir))
os.system(f'asar extract {p}/.temp/boostrap/app.asar {p}/src/boostrap')
os.system(f'asar extract {p}/.temp/app/core.asar {p}/src/app')
print('unpack ok ')