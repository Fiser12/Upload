from flask_restful import Resource,reqparse
from werkzeug.datastructures import FileStorage

from service.Upload_Service import Upload_Service

# Define the required values: the file and the expiring date
parser=reqparse.RequestParser()
parser.add_argument("file",type=FileStorage,location="files",required=True,help="File is needed")
parser.add_argument("expiring_date",type=float,location="form",required=True,help="Needed and should be decimal")
upload_Service=Upload_Service()

class Upload_Resource(Resource):
    # METHOD POST
    # id = owner of the file
    def post(self,id):
        # Request for the required values, if such values doesn't exist, it generates an error depending
        # on the missing value
        args=parser.parse_args()
        response=upload_Service.createFile(id_user=id, file=args["file"], expiring_date=args["expiring_date"])
        return response
