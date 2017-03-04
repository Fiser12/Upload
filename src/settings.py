# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST','DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
Users = {
	'schema': {
        	'Name': {
            		'type': 'string',
            		'minlength': 1,
	            	'maxlength': 50,
        	},
			'Email': {
				'type': 'email',
				'required': True,
				'unique': True,
			},
			'Salt': {
				'type': 'string',
				'minlength': 1,
				'maxlength': 50,
			},
			'Hash': {
				'type': 'string',
				'minlength': 1,
				'maxlength': 50,
			}
    	}
}
Files={
	'cache_control': 'max-age=10,must-revalidate',
    	'cache_expires': 10,
	'schema': {
		'Name': {
            'type': 'string',
			'minlength': 1,
			'maxlength': 50,
		},
        'Extension': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'Size': {
            'type': 'dict',
            'schema':{
                'number':{'type':'number'},
                'unit':{
                    'type':'list',
                    'allowed':['B','kB','MB','GB']
                }
            }
        },
        'Uploaded_date': {
            'type': 'datetime',
        },
        'Expiring_date': {
            'type': 'datetime',
        },
        'Owner_ID': {
            'type': 'objectid',
			'required': True,
            'data_relation': {
	            'resource': 'users',
                'embeddable': True
            },
		}
	}
}

DOMAIN = {'users':Users,'files': Files}
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = '172.17.0.3'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = 'afmesag'
#MONGO_PASSWORD = '1234'

MONGO_DBNAME = 'upload_db'
