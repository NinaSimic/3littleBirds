import os

from flask.app import Flask
from flask.wrappers import Response
from flask_cors.extension import CORS
from flask_jsonschema_validator.jsonschemavalidator import JSONSchemaValidator
from flask_restful import Api
import jsonschema




app = Flask(__name__)
CORS(app)
api = Api(app)

JSONSchemaValidator( app = app, root = "../res/schemas" )


@app.errorhandler( jsonschema.ValidationError )
def onValidationError( e ):
    return Response( "There was a validation error: " + str( e ), 400 )

import services.services

