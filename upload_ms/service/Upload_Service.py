import httplib
from couchdb import Server
from model.File import File

class Upload_Service():

    # id_user = owner of the file
    # file = file itself
    # expiring_date = date in seconds since the Epoch
    def createFile(self,id_user,file,expiring_date):
        # Extract the important information of the file
        fileName=file.filename
        extension=fileName[fileName.rfind(".")+1:]
	database=Server("http://192.168.99.101:3010")["blinkbox_files"]
	dataFile=file.stream.read()
        # Create a File
        newFile=File(name=file.filename,extension=extension,expiring_date=expiring_date,owner_id=id_user)
        # Try to create the documment and upload the file, if there is an error in creating or uploading, return a 500
        try:
            # Create a documment with the information of the file
            newFile.store(database)
            # Upload the file
            database.put_attachment(doc=newFile,filename=fileName,content=dataFile)
            return {"ok":True,"_id":newFile["_id"],"_rev":newFile["_rev"]}
        except:
            return {"error":httplib.INTERNAL_SERVER_ERROR}

    def getConnection(url):
	print url
	return
        try:
            return Server(url)
        except:
            return "failed"
