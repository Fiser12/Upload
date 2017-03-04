from eve import Eve
import json
from eve.io.mongo import Validator
import re
class MyValidator(Validator):
    def _validate_type_email(self,field,value):
        pattern ="[^@]+@[^@]+\.[^@]+"
        if not re.match(pattern,value):
            self._error(field,"Bad format Email")
def post_users(request, payload):
    items=json.loads(payload.get_data())["_items"]
    if len(items)>0:
        for index in items[0]:
            print index," = ",items[0][index]

def post_files(request, payload):
    items=json.loads(payload.get_data())["_items"]
    if len(items)>0:
        for index in items[0]:
            print index," = ",items[0][index]

app = Eve(validator=MyValidator)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
