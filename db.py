import os
import sqlite3
import datetime


class archdb(object):
    def __init__(self,dbname,dbtype):
        self.dbname = dbname
        self.dbtype = dbtype

        if dbtype=='sqlite':
            if os.path.exists(dbname)!=True:
                conn = sqlite3.connect(dbname)
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE files (filepath text primary key,crdate datetime,size integer) ')
                print('Create new db')
        elif dbtype=='json':
            if os.path.exists(dbname)!=True:
                a=1

    def inserttodb(self,filename):
        #pfilename = filename.replace('/','#')
        qfind = "SELECT * FROM files WHERE files.filepath=?"
        qupdate = "update files set date='%s',size=%f where path='%s'"
        qinsert =  "insert into files (filepath,crdate,size) values (?,?,?)"
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        rez = cursor.execute(qfind,(filename,))
        rez.fetchall()
        print(rez.fetchall())
        if cursor.rowcount<=0:
            ct = os.path.getctime(filename)
            sz = os.path.getsize(filename)
            #rint(qinsert%(pfilename,ct,sz))
            cursor.execute(qinsert,(filename,datetime.datetime.fromtimestamp(ct),sz))
            conn.commit()
        conn.close()
    def listbase(self):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        cursor.execute('select * from files')
        print(cursor.fetchall())