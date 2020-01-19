import os
from config import DIRS
import db

adb = db.archdb('arch.db')

for dir in DIRS:
    for root,path,files in os.walk(dir):
        for file in files:
            fullname = os.path.join(root,file)
            adb.inserttodb(fullname)
adb.listbase()
