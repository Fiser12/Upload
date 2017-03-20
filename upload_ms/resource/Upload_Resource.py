from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from service.Upload_Service import Upload_Service
from flask import Response
from json import dumps

# Define the required values: the file and the expiring date
parser = reqparse.RequestParser()
parser.add_argument("file", type=FileStorage, location="files", required=True, help="File is needed")
parser.add_argument("expiring_date", type=float, location="form", required=True,
                    help="Expiring date is needed and have to be decimal")


class Upload_Resource(Resource):
    # METHOD POST
    # id = owner of the file
    def post(self, id):
        # Request for the required values, if such values doesn't exist, it generates an error depending on the missing value
        args = parser.parse_args()
        service = Upload_Service(id_user=id, file=args["file"], expiring_date=args["expiring_date"])
        response = service.createFile()
        json_response = dumps(response["Message"], separators=(",", ":"), indent=4, sort_keys=True)
        return Response(response=json_response, status=response["Code"], content_type="application/json")
