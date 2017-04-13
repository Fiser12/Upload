import os

from flask import Flask
from flask_restful import Api
from resource.Upload_Resource import Upload_Resource

try:
    HOST_URL = os.environ['HOST_URL']
except:
    HOST_URL = "127.0.0.1"
try:
    HOST_PORT = int(os.environ['HOST_PORT'])
except:
    HOST_PORT = 4015

app = Flask(__name__);
api = Api(app)
# Define route for upload
api.add_resource(Upload_Resource, "/upload/<string:id>")

if __name__ == "__main__":
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host=HOST_URL, port=HOST_PORT)
