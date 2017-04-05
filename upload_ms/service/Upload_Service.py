import httplib
import os
from couchdb import Server
from model.File import File

try:
    DB_URL = os.environ['DB_URL']
except:
    DB_URL = "localhost"
try:
    DB_PORT = os.environ['DB_PORT']
except:
    DB_PORT = "5984"
try:
    DB_NAME= os.environ['DB_NAME']
except:
    DB_NAME="blinkbox_files"

class Upload_Service():
    # id_user = owner of the file
    # file = file itself
    # expiring_date = date in seconds since the Epoch
    def __init__(self, id_user, file, expiring_date):
        # Getting the server and then the database
        server = self.getConnection("http://"+DB_URL+":"+DB_PORT)
        if server == "failed":
            self.response = {"Code": httplib.BAD_REQUEST, "Message": "No server"}
            self.database = None
        else:
            self.database = self.getDatabase(server, DB_NAME)
            self.owner_id = id_user
            self.file = file
            self.expiring_date = expiring_date

    def createFile(self):
        if self.database == None:
            return self.response
        # Extract the important information of the file
        fileName = self.file.filename
        extension = fileName[fileName.rfind(".") + 1:]
        dataFile = self.file.stream.read()
        # Create a File
        newFile = File(name=self.file.filename, extension=extension, size=len(dataFile),
                       expiring_date=self.expiring_date, owner_id=self.owner_id)
        # Try to create the documment and upload the file, if there is an error in creating or uploading,return a 500
        try:
            # Create a documment with the information of the file
            newFile.store(self.database)
            # Upload the file
            self.database.put_attachment(doc=newFile, filename=fileName, content=dataFile)
            newFile = self.database.get(newFile["_id"])
            md5=newFile["_attachments"][fileName]["digest"]
            newFile["md5"]=md5.split("-")[1]
            self.database.save(newFile)
            return {"Code": httplib.CREATED, "Message": {"_id":newFile["_id"],"_rev":newFile["_rev"]}}
        except:
            return {"Code": httplib.INTERNAL_SERVER_ERROR, "Message": "Error upload"}

    def getConnection(self, url):
        try:
            newServer = Server(url)
            newServer.resource.head()
            return newServer
        except:
            return "failed"

    def getDatabase(self, server, name):
        try:
            return server[name]
        except:
            print "Database not found: ", name
            newDatabse = server.create(name)
            print "Database created: ", name
            return newDatabse
