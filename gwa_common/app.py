from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from gwa_framework.app import GWAApp

from gwa_common.resources import resources_v1
from gwa_common.settings import PORT, DEBUG, GWAAppConfig, GWA_ENVIRONMENT

app = GWAApp(__name__)
GWAAppConfig(app)
CORS(app)
db = SQLAlchemy(app)

# version 1
bp_v1 = Blueprint('v1', __name__, url_prefix='/v1')
api_v1 = Api(bp_v1)
app.register_blueprint(bp_v1)

if __name__ == '__main__':

    for resource_v1 in resources_v1:
        if GWA_ENVIRONMENT == 'hml':
            print(f' * Urls: {["/v1" + url for url in resource_v1["urls"]]}, '
                  f'Resource: {resource_v1["resource"].__name__}')
        api_v1.add_resource(resource_v1['resource'], *resource_v1['urls'], endpoint=resource_v1['endpoint'])
    app.run(debug=DEBUG, port=PORT)
