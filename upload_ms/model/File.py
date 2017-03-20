from couchdb.mapping import Document, TextField, DecimalField, ListField, IntegerField
from time import time, mktime
from datetime import datetime, timedelta


def expiring():
    newDate = datetime.now()+timedelta(days=7)
    return mktime(newDate.timetuple())

class File(Document):
    # Fields of the documment File
    name = TextField()
    extension = TextField()
    size = IntegerField()
    # If the upload_date isn't given, upload_date will be the today date in seconds since the Epoch
    uploaded_date = DecimalField(default=time)
    # If the expiring_date isn't given, expiring_date will be today date in a week in seconds since the Epoch
    expiring_date = DecimalField(default=expiring)
    owner_id = TextField()
    shared = ListField(TextField())
