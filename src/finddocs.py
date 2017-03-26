from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pymongo import MongoClient
import json

class FindDocsPage(QTextEdit):
    def __init__(self):
        super(FindDocsPage,self).__init__()

        self.dbname='test'
        self.collname=''

    def set_db_and_coll(self,dbname,collname):
        self.dbname=unicode(dbname)
        self.collname=unicode(collname)

        print self.dbname
        print self.collname

        mongo=MongoClient()
        db = mongo[self.dbname]
        coll=db[self.collname]

        text=QString()
        for doc in coll.find():
            text.append(str(doc))
            text.append('\n')
        self.setText(text)
        mongo.close()

    def refresh(self):
        mongo=MongoClient()
        coll=mongo[self.dbname][self.collname]
        text=QString()
        for doc in coll.find():
            text.append(str(doc))
            text.append('\n')
        self.setText(text)
        mongo.close()
