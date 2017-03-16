from couchdb.mapping import Document, TextField,DecimalField,ListField
from time import time

class File(Document):
    # Fields of the documment File
    name = TextField()
    extension = TextField()
    # If the upload_date isn't given, upload_date will be the today date in seconds since the Epoch
    uploaded_date = DecimalField(default=time)
    # If the expiring_date isn't given, expiring_date will be today date in a week in seconds since the Epoch
    expiring_date = DecimalField(default=time()+(7*24*60*60))
    owner_id = TextField()
    shared=ListField(TextField())
