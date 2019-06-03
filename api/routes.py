from flask import Blueprint, Flask, jsonify

bp = Blueprint('api', __name__)
app = Flask(__name__)


@bp.route('/flight/<string:departure>/<int:id>', methods=['GET'])
def get_user(departure, id):
    return jsonify({'departure': departure, 'ides': id})


@bp.route('/test', methods=['GET'])
def get_users():
    return jsonify({'result': 'okkk'})
