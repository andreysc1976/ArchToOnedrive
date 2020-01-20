import os
from config import DIRS,dbtype
from cred import PASS
import db,onedrive


adb = db.archdb('arch.db',dbtype)
od = onedrive.onedrive('123','andreysc@yandex.ru')

print(PASS)

for dir in DIRS:
    for root,path,files in os.walk(dir):
        for file in files:
            fullname = os.path.join(root,file)
            #adb.inserttodb(fullname)
adb.listbase()
