from api import create_app
from flasgger import Swagger

app = create_app('app')
app.config['SWAGGER'] = {
    "title": "Disk API",
    "description": "Disk API",
    "version": "0.0.1",
    "termsOfService": "",
    "hide_top_bar": True,
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Add a jwt with ** Bearer token"
        }
    },
    "security": "Bearer Auth"
}
Swagger(app)

from api.extention import db
@app.route('/')
def index():
    db.create_all()
    return 'ok'

if __name__ == '__main__':
    certificate_path = 'keys/server.crt'
    private_key_path = 'keys/server.key'

    app.run(debug=True, host='127.0.0.1', port=5000)