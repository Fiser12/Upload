from flask import Flask
from resource.Upload_Resource import Upload_Resource
from flask_restful import Api

app = Flask(__name__);
api = Api(app)
# Define route for upload
api.add_resource(Upload_Resource, "/upload/<string:id>")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4015)
