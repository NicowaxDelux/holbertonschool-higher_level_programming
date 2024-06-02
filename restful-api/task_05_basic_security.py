#!/usr/bin/python3

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from functools import wraps
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

# Configuraciones
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta_para_jwt'  # Cambia esto a una clave secreta fuerte

# Inicialización de JWT
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# User data with hashed passwords and roles
users = {
    "alice": {"password": generate_password_hash("password1"), "role": "admin"},
    "bob": {"password": generate_password_hash("password2"), "role": "user"}
}

# Autenticación Básica
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route('/', methods=['GET'])
def index():
    return jsonify(message="Welcome to the Flask API"), 200


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200

# JWT Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Credenciales inválidas"}), 401

# Función auxiliar para verificar el rol del usuario
def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            identidad = get_jwt_identity()
            rol_usuario = identidad["role"]
            if rol_usuario != role:
                return jsonify({"message": "Acceso prohibido: Rol insuficiente"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# Ruta protegida por JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", logged_in_as=current_user), 200

# Ruta accesible solo para administradores
@app.route('/admin-only', methods=['GET'])
@jwt_required()
@role_required('admin')
def admin_only():
    return jsonify(message="Admin Access: Granted"), 200

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401

# Custom error handler for accessing protected routes with invalid or missing JWT tokens
@jwt.unauthorized_loader
def unauthorized_loader_callback(callback):
    return jsonify({"error": "Unauthorized access"}), 401

# Custom error handler for accessing admin-only route with non-admin token
@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": "Forbidden access"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)
