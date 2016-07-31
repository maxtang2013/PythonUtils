import io
import os

filelist = []
for (dirpath, dirnames, filenames) in os.walk('.'):
    for f in filenames:
        if f.endswith('.png'):
            filelist.append(os.path.abspath(dirpath) + '/' + f + '\n')

txtfile = open('filelist.txt', 'w')

txtfile.writelines(filelist)

for file in filelist:
    if file.endswith('_L.png\n'):
        truefile = file.replace('\n', '')
        target = truefile.replace('_L.png', '_L1.png')
        cmd = 'PngScaler_Cleaner.exe ' + truefile + ' ' + target + ' 1'
        print (cmd + '\n')
        os.system(cmd)
