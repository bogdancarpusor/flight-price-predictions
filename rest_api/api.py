from flask import Blueprint, Flask, jsonify

bp = Blueprint('api', __name__)
app = Flask(__name__)


@bp.route('/flight/<string:departure>/<int:id>', methods=['GET'])
def get_user(departure, id):
    return jsonify({'departure': departure, 'ide': id})


@bp.route('/test', methods=['GET'])
def get_users():
    return jsonify({'result': 'okkk'})


def start_api_server():
    app.register_blueprint(bp, api_prefix='/api')
    app.run(debug=True, host='0.0.0.0')
