#ZIP File Creation
#-----------------------------------
import zipfile
'''try:
    with zipfile.ZipFile('d:/demo.zip','w',compression=zipfile.ZIP_DEFLATED) as file1:
        file1.write('d:/demo/pic1.bmp')
        file1.write('d:/demo/sample.txt')
        file1.write('d:/demo/p1.py')

except Exception:
        print("syntax error/folder does not exist/folder already zipped")

else:
    print("!!------folder zipped successfully--------!!")
'''

#zip File Extraction
#--------------------------------------
'''try:
    with zipfile.ZipFile('d:/demo.zip','r') as file2:
        file2.extractall('d:/demo')

except Exception:
        print("syntax error/folder does not exist/folder already unzipped")

else:
    print("!!------folder Unzipped successfully--------!!")
'''

#Extract Any file like gzip, tar, xz2, zip, bzip
#------------------------------------------------
import shutil
'''
shutil.make_archive('d:/backup','gztar','d:/demo')
print("!!------folder archived successfully--------!!")

shutil.unpack_archive('d:/backup.tar.gz','d:/restore_backup')
print("!!------folder unarchived successfully--------!!")
'''

#Convert zip file from Web
import requests
import zipfile
'''
url='any zip file link from github'
r=requests.get(url)
with open('d:/web.zip','wb') as file3:
    file3.write(r.content)
    print("!!-----Webfile successfully zipped-----!!")
'''

with zipfile.ZipFile('d:/web.zip','r') as file3:
    print(file3.namelist())